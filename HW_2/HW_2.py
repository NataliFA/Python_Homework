# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. *Пример:* 0,56 -> 11

n = str(input('Enter number: '))


def sum_digit_in_number(num: str):
    sum = 0
    for i in num:
        if i.isdigit():
            sum = sum + int(i)
    return sum


print(sum_digit_in_number(n))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:* пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter number: '))


def product_of_numbers(number):
    list_numbers = []
    res = 1
    for i in range(1, number+1):
        res = res * i
        list_numbers.append(res)
    return list_numbers


print(product_of_numbers(n))

# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму .
# *Пример:* Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

num = int(input('Enter number: '))


def sequence_of_numbers(n):
    lst_numbers = []
    for i in range(1, n+1):
        res = (1+1/i)**i
        lst_numbers.append(res)
    return lst_numbers


def list_like_dictionary(data: list):
    d = {}
    for a in range(1, len(data) + 1):
        d[a] = l[a-1]
    return d


l = sequence_of_numbers(num)
print(list_like_dictionary(l))

# ниже упрощенный вариант записи
# d = {int(a): l[a-1] for a in range(1, len(l) + 1)}
# d = {a: ((1+1/a)**a) for a in range(1, num + 1)}

# 4. Реализуйте выдачу случайного числа (или алгоритм перемешивания списка) не использовать random.randint и вообще библиотеку random.
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности.

import time

n = int(input('Enter number: '))


def creation_lst_num(size: int):
    lst_numbers = []
    for i in range(1, size + 1):
        a = time.time()
        time.sleep(0.01)
        b = int(a*10000 % 1 * 100 * i)
        lst_numbers.append(b)
    return lst_numbers


print(creation_lst_num(n))
