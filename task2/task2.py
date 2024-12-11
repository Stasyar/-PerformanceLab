import math
import sys


def read_circle(file_path):
    """Считывает данные окружности из файла."""
    with open(file_path, 'r') as file:
        center = tuple(map(float, file.readline().strip().split()))
        radius = float(file.readline().strip())
    return center, radius


def read_points(file_path):
    """Считывает координаты точек из файла."""
    with open(file_path, 'r') as file:
        points = [tuple(map(float, line.strip().split())) for line in file]
    return points


def point_position(center, radius, point):
    """Вычисляет положение точки относительно окружности."""

    distance = math.hypot(point[0] - center[0], point[1] - center[1])

    if math.isclose(distance, radius):
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main(circle_file, dot_file):
    center, radius = read_circle(circle_file)
    points = read_points(dot_file)

    results = [point_position(center, radius, point) for point in points]

    for result in results:
        print(result)


if __name__ == "__main__":
    print('Введите пути к файлам через пробел (1 файл с данными об окружности, '
          '2 файл с данными о точке): ')
    input_data = sys.stdin.readline().split()

    main(circle_file=input_data[0], dot_file=input_data[1])

