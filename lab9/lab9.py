# Лабораторна робота № 9. Файли (скрипти) та файли-функції (модулі). Варіант № 4
# Площа трикутника за формулою Герона: функція calculation_heron_area і програма, яка її викликає
import math


def calculation_heron_area(side_a, side_b, side_c):
    """
    Обчислює площу трикутника за формулою Герона.
    Аргументи:
      side_a, side_b, side_c (float): довжини сторін трикутника.
    Повертає:
      float: площа трикутника S.
    """
    # Обчислення півпериметра: p = (a + b + c) / 2
    semi_perimeter = (side_a + side_b + side_c) / 2
    # Обчислення площі: S = sqrt(p(p - a)(p - b)(p - c))
    area = math.sqrt(semi_perimeter * (semi_perimeter - side_a)
                     * (semi_perimeter - side_b) * (semi_perimeter - side_c))
    return area


if __name__ == "__main__":
    i = 0
    sides = []
    while i < 3:
        side = float(input("Введіть сторону: "))
        sides.append(side)
        i += 1
    print("Сторони трикутника: ", sides)

    side_a, side_b, side_c = sides
    # трикутник існує, якщо сторони додатні і кожна менша за суму двох інших
    if (side_a > 0 and side_b > 0 and side_c > 0
            and side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        area = calculation_heron_area(side_a, side_b, side_c)   # виклик функції
        print("Площа трикутника: ", area)
    else:
        print("Такого трикутника не існує")
