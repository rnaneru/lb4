import json
import xml.etree.ElementTree as ET

tree = ET.parse('persons.xml')
persons = tree.getroot()

persons_list = [
    dict((attr.tag, attr.text) for attr in person)
    for person in persons
]

with open('persons.json', 'w') as fp:
    json.dump(persons_list, fp, ensure_ascii=False, indent=4)