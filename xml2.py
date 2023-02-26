import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open("nouns.txt", "w", encoding="utf-8") as d:
    for tokens in root.iter("tokens"):
        for token in tokens.findall("token"):
            noun = []
            for g in token.iter('g'):
                noun.append(g.attrib['v'])
            if 'NOUN' in noun and 'plur' in noun:
                d.write(token.attrib['text']+"\n")
