import numpy as np

# # TODO 5.0 С клавиатуры вводятся целое 𝑎 и целое положительное 𝑛. Вычислить и вывести
# # на экран a^n
#
# a = input()
# n = input()
#
# if a.isnumeric() and n.isnumeric:
#     print(pow(int(a),int(n)))
# else:
#     print("Неверный формат данных!")
import numpy as np

# # TODO 5.1 С клавиатуры вводятся целое положительное 𝑎 и целое положительное 𝑑. Вычислить и вывести на экран частное 𝑞 и остаток 𝑟 при делении 𝑎 на 𝑑, не
# # используя операций целочисленного деления.
#
# a = input()
# d = input()
# q = 0
# r = 0
# s =0
# i =0
# if a.isnumeric() and d.isnumeric:
#     if int(a)>=0 and int(d)>=0:
#         # q = round(int(a)/int(d))
#         while s <= int(a):
#             i += 1
#             s = int(d) * i
#
#         q = i-1
#         r = int(a) - int(d)*(i-1)
#         print(q, r)
#     else:
#         print("Неверный формат данных!")
# else:
#     print("Неверный формат данных!")

# TODO 5.2 Вычислить и вывести на экран число Фибоначчи Fib𝑛, приняв с клавиатуры
# целое неотрицательное 𝑛. Рекурсивных функций не использовать, положить
# Fib0 = 0, Fib1 = 1. Предусмотреть возможное переполнение целого числа при
# решении.
#
# n = input()
# prev_1= 1 #на один шаг назад
# prev_2 = 0 #на два шага назад
# Fib = 0
# if n.isnumeric:
#     if int(n)>=0:
#         n = int(n)
#         for i in range(2, n+1):
#             Fib = prev_1 + prev_2
#             prev_2 = prev_1
#             prev_1 = Fib
#         print(Fib)
#
#     else:
#         print("Неверный формат данных!")
# else:
#     print("Неверный формат данных!")

# # TODO 5.3 Приняв с клавиатуры два натуральных числа, 𝑎 и 𝑏, вычислить и вывести на
# # экран наибольший общий делитель оных.
#
# a = input()
# b = input()
# N = 0
# if a.isnumeric() and b.isnumeric:
#     if int(a)>=0 and int(b)>=0:
#         a = int(a)
#         b = int(b)
#         M = max(a,b)
#         for i in range(1, M):
#             if a%i == 0 and b%i ==0:
#                 N = i
#             i+=1
#         print(N)
#
#     else:
#         print("Неверный формат данных!")
# else:
#     print("Неверный формат данных!")

# TODO 5.4 Составить программу для печати разложения на простые множители заданного натурального
#  числа 𝑛. При 𝑛 = 1 ничего не печатать
#
# n = input()
# N = []
#
# if n.isnumeric():
#     if int(n)>=0:
#         n = int(n)
#         for i in range(2, n):
#             if n%i == 0:
#                 N.append(i)
#                 n = n/i
#                 while n%i == 0:
#                     n = n/i
#             i+=1
#         print(N)
#
#     else:
#         print("Неверный формат данных!")
# else:
#     print("Неверный формат данных!")

# TODO 5.5 Составить программу, распечатывающую вводимое с клавиатуры натуральное
# 𝑛, полагая, что функцию printf можно вызывать только для печати цифр числа:
# вызов printf("%d", i) можно осуществлять лишь при 𝑖 = 0, 1, 2, . . . , 9.

# n = input()
# N = []
#
# if n.isnumeric():
#     p = len(n)
#     if int(n)>=0:
#         # n = int(n)
#         for i in range(0, p):
#             print(n[i])
#     else:
#         print("Неверный формат данных!")
# else:
#     print("Неверный формат данных!")