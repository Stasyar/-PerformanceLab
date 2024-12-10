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


print(main('numbers.txt'))

