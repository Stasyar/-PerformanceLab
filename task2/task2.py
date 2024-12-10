import math


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
    x_center, y_center = center
    x, y = point

    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)

    if math.isclose(distance, radius):
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    center, radius = read_circle('circle.txt')
    points = read_points('dot.txt')

    results = [point_position(center, radius, point) for point in points]

    for result in results:
        print(result)


if __name__ == "__main__":
    print(main())
