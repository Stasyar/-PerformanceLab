import json
import sys


def deserialization(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def recurs_search(tests_dict, values_dict):
    tests = tests_dict.get('tests', [])
    values = values_dict.get('values', [])

    values_map = {value['id']: value['value'] for value in values}

    def update_values(test_list):
        for test in test_list:
            test_id = test.get('id')

            if test_id in values_map:
                test['value'] = values_map[test_id]

            if 'values' in test:
                update_values(test['values'])

    update_values(tests)
    return tests_dict


def main(tests_file, values_file, report_file):
    tests = deserialization(tests_file)
    values = deserialization(values_file)

    report_dict = recurs_search(tests, values)

    with open(report_file, 'w', encoding='utf-8') as file:
        json.dump(report_dict, file, indent=2)


if __name__ == "__main__":
    print('Введите пути к файлам через пробел (1 файл с данными о тестах, 2 файл с '
          'данными значениях, 3 файл для записи результата')
    input_data = sys.stdin.readline().split()

    main(tests_file=input_data[0], values_file=input_data[1], report_file=input_data[2])
