"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""
import csv
from pathlib import Path

current_dir = Path(__file__).parent
file_path_r_m_c = current_dir / 'r-m-c.csv'
file_path_rmc = current_dir / 'rmc.csv'


def read_csv(file_path, delimiter):
    with open(file_path, newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=delimiter))

    headers = data[0]
    return [dict(zip(headers, row)) for row in data[1:]]


file_1 = read_csv(file_path_r_m_c, ',')
file_2 = read_csv(file_path_rmc, ';')

headers_file_1  = file_1[0].keys()
headers_file_2  = file_2[0].keys()

def unique_data():

    unique_data = []
    for row in file_1:
        if row not in unique_data:
            unique_data.append(row)


    for row in file_2:
        if row not in unique_data:
            unique_data.append(row)


    headers_result = []
    for header in headers_file_1:
        if header not in headers_result:
            headers_result.append(header)

    for header in headers_file_2:
        if header not in headers_result:
            headers_result.append(header)

    return headers_result, unique_data

headers_result, unique_data = unique_data()

result_file_csv = current_dir / 'result_file_csv.csv'
with open(result_file_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(headers_result)

    for row in unique_data:
        writer.writerow(row.values())