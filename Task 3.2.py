import math

eps = 1E-5

# 5.0 Принять с клавиатуры координаты 𝑥𝑎, 𝑦𝑎, 𝑥𝑏, 𝑦𝑏, 𝑥𝑐, 𝑦𝑐 треугольника 𝑎𝑏𝑐 на
# плоскости. Определить тип треугольника и вывести на экран целое число в
# зависимости от ответа: 0 — остроугольный, 1 — прямоугольный, 2 — тупоугольный.
#
# x_A = float(input())
# y_A = float(input())
# x_B = float(input())
# y_B = float(input())
# x_C = float(input())
# y_C = float(input())
#
# a = round(math.sqrt((x_C - x_B)**2 + (y_C - y_B)**2), 6)
# b = round(math.sqrt((x_A - x_C)**2 + (y_A - y_C)**2), 6)
# c = round(math.sqrt((x_B - x_A)**2 + (y_B - y_A)**2), 6)
#
# len_1 = max(max(a, b), max(a, c))
# len_2 = min(a, b)
# len_3 = min(a,c)
#
# print(len_1, len_2, len_3)
#
# if len_1**2 - (len_2**2 + len_3**2) < eps:
#     print('1')
# elif len_1 ** 2 < len_2 ** 2 + len_3 ** 2:
#     print('0')
# elif len_1**2 > len_2**2 + len_3**2:
#     print('2')
# else:
#     print("Треугольник не существует!")
#
# 5.1 Принять с клавиатуры координаты 𝑥𝑎, 𝑦𝑎, 𝑥𝑏, 𝑦𝑏, 𝑥𝑐, 𝑦𝑐 треугольника 𝑎𝑏𝑐 на
# плоскости. Найти и вывести на экран площадь 𝑆 треугольника
#
# x_A = float(input())
# y_A = float(input())
# x_B = float(input())
# y_B = float(input())
# x_C = float(input())
# y_C = float(input())
#
# a = math.sqrt((x_C - x_B)**2 + (y_C - y_B)**2)
# b = math.sqrt((x_A - x_C)**2 + (y_A - y_C)**2)
# c = math.sqrt((x_B - x_A)**2 + (y_B - y_A)**2)
# print(a,b,c)
#
# cos_alfa = (a**2 + b**2 - c**2)/(2*a*b)
# alfa = math.acos(cos_alfa)
# S = 0.5 * a * b * math.sin(alfa)
# print(S)



# 5.2 С клавиатуры задаются координаты 𝑥𝑎, 𝑦𝑎, 𝑥𝑏, 𝑦𝑏, 𝑥𝑐, 𝑦𝑐 вершин треугольника 𝑎𝑏𝑐 на плоскости и координаты точки 𝑥𝑝, 𝑦𝑝. Определить, лежит ли точка
# внутри, на границе или вне треугольника, и вывести на экран 0, 1 или 2 соответственно.
#
# x_A = float(input())
# y_A = float(input())
# x_B = float(input())
# y_B = float(input())
# x_C = float(input())
# y_C = float(input())
#
# x_p = float(input())
# y_p = float(input())
#
# a = (x_A-x_p)*(y_B-y_A)-(x_B-x_A)*(y_A-y_p)
# b = (x_B-x_p)*(y_C-y_B)-(x_C-x_B)*(y_B-y_p)
# c = (x_C-x_p)*(y_A-y_C)-(x_A-x_C)*(y_C-y_p)
#
# if a ==0 or b== 0 or c == 0:
#     print('1 -- на границе')
# elif a*b > 0 and b*c>0:
#     print('0 -- внутри треугольника')
# else:
#     print('2 -- вне треугольника')



# 5.3 . С клавиатуры задаются координаты точек 𝑥𝑞, 𝑦𝑞, 𝑥𝑟, 𝑦𝑟 на прямой и координаты произвольной точки 𝑥𝑝, 𝑦𝑝. Определить взаимное расположение точки и
# прямой и вывести на экран целое число в зависимости от ответа: 0 — лежит
# выше прямой, 1 — на прямой, 2 — ниже прямой.

# x_A = float(input())
# y_A = float(input())
# x_B = float(input())
# y_B = float(input())
#
# x_p = float(input())
# y_p = float(input())
#
# k = (y_B - y_A)/(x_B - x_A)
#
# if y_p == k*(x_p - x_A) + y_A:
#     print('on line')
# elif y_p < k*(x_p - x_A) + y_A:
#     print('under line')
# else:
#     print('up line')


# 5.4 С клавиатуры задаются координаты точек 𝑥𝑞, 𝑦𝑞, 𝑥𝑟, 𝑦𝑟 отрезка 𝑞𝑟 и координаты произвольной точки 𝑥𝑝, 𝑦𝑝.
#  Определить, не принадлежит или принадлежит точка отрезку,
#  и вывести на экран 0 или 1 соответственно.

# x_A = float(input())
# y_A = float(input())
# x_B = float(input())
# y_B = float(input())
#
# x_p = float(input())
# y_p = float(input())
#
# k = (y_B - y_A)/(x_B - x_A)
#
# if y_p == k*(x_p - x_A) + y_A:
#     if x_A < x_p< x_B or x_B<x_p<x_A:
#         if y_A < y_p < y_B or y_B < y_p < y_A:
#             print('1 -- принадлежит')
#         else:
#             print('0 -- не принадлежит')
#     else:
#         print('0 -- не принадлежит')
#
# else:
#     print('0 -- не принадлежит')

# 5.5 С клавиатуры задаются координаты точек 𝑥𝑝, 𝑦𝑝, 𝑥𝑞, 𝑦𝑞 отрезка 𝑝𝑞 и координаты точек 𝑥𝑟, 𝑦𝑟, 𝑥𝑠, 𝑦𝑠 отрезка 𝑟𝑠.
# Определить, не пересекаются или пересекаются два отрезка, и вывести на экран 0 или 1 соответственно. Под пересечением
# понимать точку, принадлежащую обоим отрезкам и не являющуюся концом
# отрезка.

