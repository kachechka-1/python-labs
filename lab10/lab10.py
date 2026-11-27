# Лабораторна робота № 10. Розгалуження в Python. Варіант № 4
#       | 2.3 * ∛(x - 1.3) + sin²x,       x > 2
#   y = | arccos(x/2) + 2^(3x),           -2 <= x <= 2
#       | |x|^sin(x) - lg|x + 1.5|,       x < -2
import math

x_value = float(input("Введіть значення x: "))

if x_value > 2:
    y_value = 2.3 * math.cbrt(x_value - 1.3) + math.sin(x_value) ** 2
elif -2 <= x_value <= 2:
    y_value = math.acos(x_value / 2) + 2 ** (3 * x_value)
else:
    y_value = abs(x_value) ** math.sin(x_value) - math.log10(abs(x_value + 1.5))

print(f"y = {y_value}")
