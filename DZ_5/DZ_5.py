#  Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии. A = 3; B = 5 -> 243 (3⁵) A = 2; B = 3 -> 8

def expo(a, b):
    if a != 0 and b == 0:
        return 1
    elif a == 0 and b == 0:
        return f'0 в степени 0 не определен'
    elif b == 1:
        return a ** 1
    else:
        return a * expo(a, b - 1)


print(expo(int(input('введи А: ')), int(input('введи B: '))))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех
# арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# def summa(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return summa(a + 1, b - 1)
#
#
# print(summa(int(input('введи А: ')), int(input('введи B: '))))