# Лабораторна робота № 9. Файли (скрипти) та файли-функції (модулі). Варіант № 4
# Площа трикутника за формулою Герона: функція calculation_heron_area і програма, яка її викликає
import math


def calculation_heron_area(a, b, c):
    """
    Обчислює площу трикутника за формулою Герона.
    Аргументи:
      a, b, c (float): довжини сторін трикутника.
    Повертає:
      float: площа трикутника S.
    """
    # Обчислення півпериметра: p = (a + b + c) / 2
    semi_perimeter = (a + b + c) / 2
    # Обчислення площі: S = sqrt(p(p - a)(p - b)(p - c))
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return area


if __name__ == "__main__":
    i = 0
    sides = []
    while i < 3:
        side = float(input("Введіть сторону: "))
        sides.append(side)
        i += 1
    print("Сторони трикутника: ", sides)

    a, b, c = sides
    # трикутник існує, якщо сторони додатні і кожна менша за суму двох інших
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        area = calculation_heron_area(a, b, c)   # виклик функції
        print("Площа трикутника: ", area)
    else:
        print("Такого трикутника не існує")
