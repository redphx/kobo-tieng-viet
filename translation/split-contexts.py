from xml.etree import ElementTree as ET
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path, help='Path to the .ts file')
    parser.add_argument(
        '--comment', type=str, default=None, help='Value for the <extracomment> tag'
    )

    args = parser.parse_args()
    file_path = args.file
    comment = args.comment

    # Start splitting
    tree = ET.parse(file_path)
    root = tree.getroot()

    current_path = Path(__file__).parent.absolute()

    for new_context in root.findall('context'):
        name_elem = new_context.find('name')
        if name_elem is None or not name_elem.text:
            continue

        output_path = current_path / 'contexts' / f'{name_elem.text}.xml'
        print(output_path)

        if not output_path.exists():
            # TODO: add <extracomment>
            # Save the entire context to file
            ET.ElementTree(new_context).write(
                output_path, encoding='utf-8', xml_declaration=False
            )
            continue

        # Merge contexts
        # Read original context
        org_context = ET.parse(output_path).getroot()

        org_sources = {
            msg.find('source').text for msg in org_context.findall('message')
        }

        for msg_b in new_context.findall('message'):
            src = msg_b.find('source').text
            if src not in org_sources:
                # Add <extracomment>
                ET.SubElement(msg_b, 'extracomment').text = comment

                org_context.append(msg_b)
                org_sources.add(src)

        ET.ElementTree(org_context).write(
            output_path, encoding='utf-8', xml_declaration=False
        )

        with open(output_path, 'a') as fp:
            fp.write('\n')


if __name__ == '__main__':
    main()
