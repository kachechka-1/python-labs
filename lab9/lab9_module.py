# Лабораторна робота № 9. Файли (скрипти) та файли-функції (модулі). Варіант № 4
# Виклик функції heron_area з модуля heron.py для кількох трикутників
import heron

# довідка (docstring) функції
print(heron.heron_area.__doc__)

# набори сторін трикутників (a, b, c)
triangles = [(3, 4, 5), (5, 6, 7), (2.5, 3, 4), (6, 8, 10)]

for a, b, c in triangles:
    # Викликаємо функцію heron_area з модуля heron
    S = heron.heron_area(a, b, c)
    print(f"При a={a}, b={b}, c={c}: Площа S={S}")
