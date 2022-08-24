from functools import reduce

from random import randint
import math

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce:

# 1. Определить, присутствует ли в заданном списке строк, некоторое число

word_list = ['Один', '2два', 'пять', 'восемь', 'девять9', '123']
num = str(input('Enter number: '))

def find_number(words: list, number: int):
    num_in_word = any([char for char in words if number in char])
    return num_in_word


print(find_number(word_list, num))


# 2. Найти сумму чисел списка стоящих на нечетной позиции

int_num_list = [randint(1, 11) for i in range(9)]
print(int_num_list)


def sum_odd_position(num_list):
    num_on_odd_position = [int_num_list[i]
                           for i in range(1, len(int_num_list), 2)]
    return reduce(lambda x, y: x + y, num_on_odd_position)


print('Sum of elements in odd positions = ', sum_odd_position(int_num_list))

# 3. Найти расстояние между двумя точками пространства(числа вводятся через пробел)

def coordinate():
    return list(map(int, input('Enter point coordinates separeted by spaces: ').split()))


def distance_two_points(coord):
    while len(coord) != 4:
        coord = coordinate()

    return round(math.sqrt((coord[1] - coord[0])**2 + (coord[3] - coord[2])**2), 2)


c = coordinate()
print(distance_two_points(c))

# 4. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

# **Примеры:**
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1

text = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]


def filter_text(text):
    a = [i for i, x in enumerate(text) if x == 'йцу']
    if len(a) == 0 or len(a) == 1:
        return -1
    return a[1]


print(filter_text(text))

# 5. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

int_num_list = [randint(1, 11) for i in range(9)]
print(int_num_list)


def mult_num(num_list):
    l = len(int_num_list)
    return [int_num_list[i]*int_num_list[l-i-1]
            for i in range(0, math.ceil(l/2))]


print(mult_num(int_num_list))

# 6. Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.


def int_number():
    while True:
        num = input('Введите число: ')
        try:
            num = int(num)
            return num
        except ValueError:
            print('Ошибка. Неправильный ввод')


def sequence_of_number():
    n = int_number()

    return [(-3) ** i for i in range(0, n)]


print(sequence_of_number())
