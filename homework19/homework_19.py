'''
Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек - наприкладTimestamp 05:45:40,
 а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)
Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один
 потік - Key TSTFEED0300|7E3E|0400
Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
       3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.
Обов’язково включіть результат роботи — файл hb_test.log в PR.
'''
from datetime import datetime
import logging


key = 'Key TSTFEED0300|7E3E|0400'

def get_heartbeat_lines(file_name):

    heartbeat_lines = []

    with open(file_name, "r") as file:
        for line in file:
            if key in line:
                heartbeat_lines.append(line)

    return heartbeat_lines

def get_timestamp(heartbeat_line):
    parts = heartbeat_line.split()
    timestamp_index = parts.index("Timestamp")
    timestamp = parts[timestamp_index + 1]

    return datetime.strptime(timestamp, "%H:%M:%S")

def time_dif(current_line, next_line):
    timestamp_current = get_timestamp(current_line)
    timestamp_next = get_timestamp(next_line)

    difference = timestamp_current - timestamp_next

    return difference.total_seconds()

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

file_handler = logging.FileHandler("hb_test.log")
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


heartbeat_lines = get_heartbeat_lines("hblog.txt")


for i in range(len(heartbeat_lines) - 1):
    seconds = time_dif(
        heartbeat_lines[i],
        heartbeat_lines[i + 1]
    )

    timestamp = get_timestamp(heartbeat_lines[i])

    if seconds > 31 and seconds < 33:
        logger.warning(
            f"Heartbeat at {timestamp.strftime('%H:%M:%S')}: {seconds} seconds"
        )

    elif seconds >= 33:
        logger.error(
            f"Heartbeat at {timestamp.strftime('%H:%M:%S')}: {seconds} seconds"
        )