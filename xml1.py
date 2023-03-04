import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('sentences.txt', 'w', encoding='utf-8') as d:
    for source in root.iter('source'):
        d.write(source.text+"\n")