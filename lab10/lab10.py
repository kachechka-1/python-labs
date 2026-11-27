# Лабораторна робота № 10. Розгалуження в Python. Варіант № 4
#       | 2.3 * ∛(x - 1.3) + sin²x,       x > 2
#   y = | arccos(x/2) + 2^(3x),           -2 <= x <= 2
#       | |x|^sin(x) - lg|x + 1.5|,       x < -2
import math

x = float(input("Введіть значення x: "))

if x > 2:
    y = 2.3 * math.cbrt(x - 1.3) + math.sin(x) ** 2
elif -2 <= x <= 2:
    y = math.acos(x / 2) + 2 ** (3 * x)
else:
    y = abs(x) ** math.sin(x) - math.log10(abs(x + 1.5))

print(f"y = {y}")
