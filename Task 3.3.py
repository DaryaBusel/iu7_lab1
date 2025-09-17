import math


#TODO Приняв с клавиатуры 𝑥 и 𝜀, 0 < 𝜀 ⩽ 1, вывести на экран вычисленное с точностью1
# 𝜀 приближённое значение 𝑠(𝑥) и точное значение 𝑓(𝑥) функции 𝑓, абсолютную
# ∆ и относительную 𝛿 погрешности:

x = float(input())
eps = float(input())

# #7.0
# sum_x = 0
# func = math.exp(x)
# i =0
# N = 1
# while abs(func - sum_x) > eps:
#     sum_x += N
#     i += 1
#     N = N * x/i
# delta_abs = abs(func - sum_x)
# delta = abs(func - sum_x)/func
# print(sum_x, func, delta_abs, delta)

# #7.1
# sum_x = 0
# func = math.sin(x)
# i =0
# N = 1
# while abs(func - sum_x) > eps:
#     N = pow(-1, i) * pow(x, 2*i+1) / math.factorial(2 * i + 1)
#     sum_x += N
#     i += 1
#     if i%50 ==0:
#         print(N, func, sum_x)
#         break
# delta_abs = abs(func - sum_x)
# delta = abs(func - sum_x)/func
# print(sum_x, func, delta_abs, delta)

#7.2
# sum_x = 0
# func = math.asin(x)
# i =0
# N = x
# for i in range(0,100):
#     sum_x += N
#     if i == 0:
#         N = 1
#     i += 1
#     N = N* pow(x, 2 * i + 1) * (2*i-1) / ((2 * i + 1)*2*i)
#     if i%50 ==0:
#         print(N, func, sum_x)
#         break
# delta_abs = abs(func - sum_x)
# delta = abs(func - sum_x)/func
# print(sum_x, func, delta_abs, delta)

# #7.3
# sum_x = 0
# func = math.atan(x)
# i =0
# N = 1
# while abs(func - sum_x) > eps:
#     N = pow(-1, i) * pow(x, 2*i+1) / (2 * i + 1)
#     sum_x += N
#     i += 1
#     if i%50 ==0:
#         print(N, func, sum_x)
#         break
# delta_abs = abs(func - sum_x)
# delta = abs(func - sum_x)/func
# print(sum_x, func, delta_abs, delta)

# 7.4
# sum_x = 0
# func = 1/pow(1+x, 3)
# i =0
# N = 1
# for i in range(0,100):
#     sum_x += N
#     i += 1
#     N = pow(-1, i) * pow(x, i) * (i +2) * (i+1) / 2
#     if i%50 ==0:
#         print(N, func, sum_x)
#
# delta_abs = abs(func - sum_x)
# delta = abs(func - sum_x)/func
# print(sum_x, func, delta_abs, delta)


# 7.5
# sum_x = 1
# func = 1/math.sqrt(1-pow(x,2))
# i =0
# N = 1
# k = 1
# for i in range(1,50):
#     k *= (2*i - 1)/ (2*i)
#     N = k*pow(x, 2*i)
#     sum_x += N
#     i += 1
#     if i%50 ==0:
#         print(N, func, sum_x)
#         break
# delta_abs = abs(func - sum_x)
# delta = abs(func - sum_x)/func
# print(sum_x, func, delta_abs, delta)

