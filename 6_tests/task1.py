def discriminant(a, b, c):
    # функция для нахождения дискриминанта
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    discr = discriminant(a, b, c)
    if discr < 0:
        return [None]
    elif discr == 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        return [x1]
    else:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return [x1, x2]
    # функция для нахождения корней уравнения


if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))