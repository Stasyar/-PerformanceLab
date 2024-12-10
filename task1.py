import sys


def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    path = ''
    current_index = 0

    while True:
        path += str(circular_array[current_index])

        next_index = (current_index + m - 1) % n

        if next_index == 0:
            break

        current_index = next_index

    return path


input_data = sys.stdin.readline().split()
n = int(input_data[0])
m = int(input_data[1])
result = circular_array_path(n, m)
print(result)





