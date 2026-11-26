import math as m
i = 0
storona = []
while  i < 3:
    side = float(input("Введіть сторону: "))
    storona.append(side)
    i += 1
print("Сторони трикутника: ", storona)

a, b, c = storona
# трикутник існує, якщо сторони додатні і кожна менша за суму двох інших
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    pivper = (a + b + c) / 2
    area = m.sqrt(pivper * (pivper - a) * (pivper - b) * (pivper - c))
    print("Площа трикутника: ", area)
else:
    print("Такого трикутника не існує")
