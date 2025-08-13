import os
from lxml import etree

dir_path = 'contexts'

combined_text = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="vi_VN">
'''

for fname in os.listdir(dir_path):
    if not fname.endswith('.xml'):
        continue

    path = os.path.join(dir_path, fname)

    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(path, parser)
    root = tree.getroot()

    messages = root.findall('message')
    messages.sort(key=lambda m: m.findtext('source', '').lower())

    for m in messages:
        root.remove(m)
    for m in messages:
        root.append(m)

    tree.write(path, encoding='utf-8', xml_declaration=False, pretty_print=True)
