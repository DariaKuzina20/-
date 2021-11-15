import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
D = b ** 2 - 4 * a * c
if a != 0:
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Корни уравнения:", x1, x2)
        print("Количество корней: 2")
    elif D == 0:
        x = -b / (2 * a)
        print("Корень уравнения:", x)
        print("Количество корней: 1")
    else:
        print("Корней нет")
else:
    x=-c/b
    print("Корень неквадратного (т.к. a=0) уравнения:", x)
    print("Количество корней: 1")
