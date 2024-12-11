import sys

def get_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = list([int(n.strip()) for n in file.readlines()])
        numbers.sort()
    return numbers


def main(file_path):
    numbers = get_numbers(file_path)
    middle = numbers[len(numbers) // 2]

    count = sum(abs(n - middle) for n in numbers)
    return count


if __name__ == "__main__":
    print('Введите путь к файлу')
    input_data = sys.stdin.readline().strip()

    print(main(input_data))

