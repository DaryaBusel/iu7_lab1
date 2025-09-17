import math

# task 1
# s = 56
# print(f'Year has {s} weeks')

# task 2
#TODO 2.0 Принять с клавиатуры величины оснований 𝑎 и 𝑏 и высоты ℎ равнобедренной
# трапеции. Найти и вывести на экран периметр 𝑃 трапеции.

# a = input()
# b = input()
# h = input()
#
# if a.isnumeric() and b.isnumeric() and h.isnumeric():
#     delta = abs(float(b)-float(a))/2
#     c = math.sqrt(float(h)**2 + delta**2)
#     print(c*2 + float(a) + float(b))
# else:
#     print("Вводить можно только число!")

#TODO 2.1 Принять с клавиатуры величины оснований 𝑎 и 𝑏 и угла в градусах 𝜙 при большем основании равнобедренной трапеции. Найти и вывести на экран площадь
# 𝑆 трапеции.

# a = input()
# b = input()
# phi = input("Введите угол в градусах:")
#
# try:
#     delta = abs(float(b) - float(a)) / 2
#     h = math.tan(math.radians(float(phi))) * delta
#     S = (float(b) + float(a)) * h / 2
#     print(S)
#
# except:
#     print("Неверный формат данных!")

#TODO 2.2 Принять с клавиатуры координаты 𝑥𝑎, 𝑦𝑎, 𝑥𝑏, 𝑦𝑏, 𝑥𝑐, 𝑦𝑐 треугольника 𝑎𝑏𝑐 на
# плоскости. Найти и вывести на экран периметр 𝑃 треугольника.

#
# try:
#     x_A = float(input())
#     y_A = float(input())
#     x_B = float(input())
#     y_B = float(input())
#     x_C = float(input())
#     y_C = float(input())
#     a = math.sqrt((x_B - x_C)**2 + (y_B - y_C)**2)
#     b = math.sqrt((x_A - x_C)**2 + (y_A - y_C)**2)
#     c = math.sqrt((x_B - x_A)**2 + (y_B - y_A)**2)
#
#     if (a+b) > c and (c+b) > a and (a+c) > b:
#         print(a+b+c)
#
#     else:
#         print("Треугольник не существует!")
#
# except:
#     print("Неверный формат данных!")

#TODO 2.3 Принять с клавиатуры величины двух сторон 𝑎 и 𝑏 треугольника 𝑎𝑏𝑐 и угла в
# градусах 𝜙 между ними. Найти и вывести на экран площадь 𝑆 треугольника.

# a = input()
# b = input()
# phi = input("Введите угол в градусах:")
#
# try:
#     S = float(a)*float(b)*math.sin(math.radians(float(phi)))/2
#     print(S)
# except:
#     print("Неверный формат данных!")

