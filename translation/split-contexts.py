from xml.etree import ElementTree as ET
from pathlib import Path

tree = ET.parse('nickel-4.42.23296-19-en.ts')
root = tree.getroot()

for context in root.findall('context'):
    name_elem = context.find('name')
    if name_elem is None or not name_elem.text:
        continue

    output_path = Path(f'contexts/{name_elem.text}.xml')
    ET.ElementTree(context).write(output_path, encoding='utf-8', xml_declaration=False)
