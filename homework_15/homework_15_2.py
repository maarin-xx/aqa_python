"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу
виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""


from pathlib import Path
import json
from logging_15_2 import logger

current_dir = Path(__file__).parent
json_dir = current_dir / 'homework_15_2_json'
files = [f for f in json_dir.iterdir() if f.is_file()]

for file in files:
    try:
        with open(file) as file:
            data = json.load(file)
    except Exception as e:
        logger.error(f'{file.name} is not valid, {e}')
