import json


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




def main():
    tests = deserialization('tests.json')
    values = deserialization('values.json')

    report_dict = recurs_search(tests, values)

    with open('report.json', 'w', encoding='utf-8') as file:
        json.dump(report_dict, file, indent=2)


if __name__ == '__main__':
    print(main())
