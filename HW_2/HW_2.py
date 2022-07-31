# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. *Пример:* 0,56 -> 11

# from function import checking_for_a_number

# n = str(checking_for_a_number('введите число: '))
# sum = 0
# for i in n:
#     if i.isdigit():
#             sum = sum + int(i)

# print(sum)

# n = str(input('введите число: '))

# def sum_digit_in_number(num:str):
#     sum = 0
#     for i in num:
#         if i.isdigit():
#             sum = sum + int(i)
#     return sum


# print(sum_digit_in_number(n))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:* пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Enter number: '))

# def product_of_numbers(number):
#     list_numbers = []
#     res = 1
#     for i in range(1, number+1):
#         res = res * i
#         list_numbers.append(res)
#     return list_numbers

# print(product_of_numbers(n))

# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму .
# *Пример:* Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

# num = int(input('Enter number: '))

# def sequence_of_numbers(n):
#     lst_numbers = []
#     for i in range(1, n+1):
#         res = (1+1/i)**i
#         lst_numbers.append(res)
#     return lst_numbers

# print(sequence_of_numbers(num))

# 4. Реализуйте выдачу случайного числа (или алгоритм перемешивания списка) не использовать random.randint и вообще библиотеку random.
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности.
# x = 37
# y = 58
# z = x & y # z = 32
# print('x = ', x)
# print('y = ', y)
# print('z = ', z)

import itertools


def XOR_cipher(string, key):

    answer = []

    key = itertools.cycle(key)

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)


print(XOR_cipher('123546846351', '0'))
