# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12.

from function import int_list_creation

num = int(input('Введите число = длине списка - '))


def sum_of_odd_position(data: list):
    sum = int(0)
    for index in range(0, len(data)):
        if index % 2 != 0:
            sum = sum + data[index]
    return sum


spisok = int_list_creation(num)
print(spisok)
print('Сумма элементов, стоящих на нечетных позициях =',
      sum_of_odd_position(spisok))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; (4 возвести в квадрат)


num = int(input('Введите число = длине списка - '))


def mult_list_elements(data: list):
    new_list_numbers = []
    l = len(data)
    for index in range(0, l//2):
        mult = data[index]*data[l-index-1]
        new_list_numbers.append(mult)
    if l % 2 != 0:
        new_list_numbers.append(data[l//2]**2)
    return new_list_numbers


spisok = int_list_creation(num)
print(spisok)
print(mult_list_elements(spisok))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

float_list_number = [1.1, 1.2, 3.1, 5.567, 10.003]


def separation_of_integer_and_fraction(data: list):
    frac_num = []
    for i in data:
        sep = i % 1
        frac_num.append(sep)
    return frac_num


def dif_max_min_num(data: list):
    min = 1
    max = 0
    for i in data:
        if i > max:
            max = i
        elif i < min:
            min = i
    res = max - min
    return res


lst_num = separation_of_integer_and_fraction(float_list_number)

print(dif_max_min_num(lst_num))

# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное. *Пример:* 45 -> 101101

num = int(input('Введите число - '))


def convert_num_in_binary(n):
    bin = str()
    while n // 2 != 0:
        bin = str(n % 2) + bin
        n //= 2
    return str(n) + bin


print(convert_num_in_binary(num))

# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число - '))


def fibonachi(n):
    fib = []
    for index in range(0, n + 1):
        if index == 0:
            fib.append(0)
        elif index == 1 or index == 2:
            fib.append(1)
        else:
            fib.append(int(fib[index - 1] + fib[index - 2]))
    return fib


def negafibonachi(data):
    negafib = []
    for index in range(len(data) - 1, 0, -1):
        if not index % 2:
            negafib.append(data[index] * (-1))
        else:
            negafib.append(data[index])
    return negafib


lst1 = fibonachi(num)
lst2 = negafibonachi(lst1)

print(lst2 + lst1)
