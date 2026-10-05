"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

from pathlib import Path
import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

current_dir = Path(__file__).parent
xml_file = current_dir / 'homework_15_3_xml' / 'groups.xml'

# Завантаження XML-файлу
tree = ET.parse(xml_file)
root = tree.getroot()


def search_income_by_group_number(group_number):
    group_number = str(group_number)
    for group in root.findall('group'):
        if group_number != 'None' and group.find('number').text == group_number:

            timingExbytes = group.find('timingExbytes')
            if timingExbytes is None:
                raise ValueError (
                    f"Group {group_number} doesn't have timingExbytes"
                )
            incoming = (timingExbytes.find('incoming')).text

            if incoming is None:
                raise ValueError(
                    f"Group {group_number} doesn't have incoming"
                )

            return incoming

    raise ValueError(f"Can't find group with number {group_number}")

try:
    result = search_income_by_group_number(2)
    logger.info(result)
except ValueError as e:
    logger.error(e)





