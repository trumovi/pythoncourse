import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

CONJ = 0
VERB = 0
for tokens in root.iter("tokens"):
    for token in tokens.findall("token"):
        if token.attrib['text'] in ["может", "Может"]:
            for word in token.iter('g'):
                if word.attrib['v'] == 'CONJ':
                    CONJ += 1
                if word.attrib['v'] == 'VERB':
                    VERB += 1
print(f"Conj = {CONJ}, Verb = {VERB}")
