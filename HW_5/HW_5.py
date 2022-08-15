# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Пример: 'абвгдейка - это передача' = >" - это передача"

import string
import random
from random import randint

sentence = 'абвгдейка - это передача, абвгдейка, абвгдейка — Это учёба и игра, абвгдейка, абвгдейка, Азбуку детям знать пора.'

print(sentence)


def del_text(s: str, text: str):
    words = s.replace(text, '1')
    word_list = list(map(str, words.split()))
    l = [word for word in word_list for i in word if i.isdigit()]
    # word_list1 = [word_list.remove(i) for i in l]
    for i in l:
        word_list.remove(i)
    return (' '.join(word_list))


print(del_text(sentence, 'абв'))

# с семинара:


def filter_text(text):
    # text = text.split()
    # func = lambda word: 'абв' not in word
    # return ' '.join(list(filter(func, text)))
    return ' '.join(list(filter(lambda word: 'абв' not in word, text.split())))


# print(filter_text(sentence))


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# отдельный файл

# 3. Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# Пример: ['python', 'c#'] [1,2]

language_name = ['python', 'c#', 'c++', 'php', 'java', 'kotlin']
num_lst = [1, 2, 3, 4, 5, 6]

# language_name = ['python', 'c#', 'php', 'c++', 'kotlin', 'java'] # для проверки
# num_lst = [1, 2, 3, 4, 5, 6]

# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. [(1,'PYTHON'), (2,'C#')]


def lst_tuple(lang: list, num: list):
    l = [el.upper() for el in lang]
    t = list(zip(num, l))
    return t

# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков. [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет] [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.


def num_of_points(lst_tuple: list, n_l: list):
    word_lst = [el[1] for el in lst_tuple]  # список слов с большой буквы
    # print(word_lst)
    # points = [lambda res: (res + ord(w[i])) for w in word_lst for i in range(0, len(w))] # Как сделать запись результата в 1 строчку?
    points = []  # список очков в каждом слове
    for w in word_lst:
        res = 0
        for i in range(0, len(w)):
            res = res + ord(w[i])
        points.append(res)
    # print(points)

    # список остатка от деления очков на цифру перед словом
    remainder = [p % num for p, num in zip(points, n_l)]

    # список индексов из списка остатков, если остаток 0, то записывает индекс
    index_list = [index for index, r in enumerate(remainder) if r == 0]

    # список слов, у которых очки делятся на цифру
    new_language_lst = [word_lst[i] for i in index_list]

    # список очков только тех слов, что указаны выше
    new_points = [points[i] for i in index_list]

    points_plus_lst_tuple = list(
        zip(new_points, new_language_lst))  # новый список кортежей

    return points_plus_lst_tuple


c = lst_tuple(language_name, num_lst)
print(num_of_points(c, num_lst))

# # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

# # когда в строке ЕСТЬ пробелы между буквами


def str_list_with_space(num):  # строка с пробелом
    num_list = [randint(1, 20) for i in range(num)]
    string_list = [random.choice(string.ascii_lowercase) for i in range(num)]
    str_num = [n*i for n, i in zip(string_list, num_list)]
    print(' '.join(str_num))  # для вывода в консоль
    return ' '.join(str_num)


def write_file_with_spaces(s_list):
    with open('HW_5\IN_data_with_spaces.txt', 'a') as file:
        file.write(f'{s_list}\n')


def letter_count(file_path):
    with open(file_path, 'r') as data:
        for line in data.readlines():
            str_word = line.strip()
        str_word = list(map(str, str_word.split()))
        # print(str_word)
        sum_letter = [str(len(s)) for s in str_word]
        # print(l)
        letter = [s[0] for s in str_word]
        # print(c)
        combination = [n+i for n, i in zip(sum_letter, letter)]
        print(''.join(combination))

    with open('HW_5\OUT_data_with_spaces.txt', 'a') as file:
        file.write(f'{"".join(combination)}\n')


l = str_list_with_space(5)
write_file_with_spaces(l)
letter_count('HW_5\IN_data_with_spaces.txt')

# когда в строке НЕТ пробелов между буквами


def str_list_without_space(num):  # строка с пробелом
    num_list = [randint(1, 10) for i in range(num)]
    string_list = [random.choice(string.ascii_lowercase) for i in range(num)]
    str_num = [n*i for n, i in zip(string_list, num_list)]
    print(''.join(str_num))  # для вывода в консоль
    return ''.join(str_num)


def write_file_without_spaces(s_list):
    with open('HW_5\In_data_without_spaces.txt', 'a') as file:
        file.write(f'{s_list}\n')


def letter_count(file_path):
    with open(file_path, 'r') as data:
        for line in data.readlines():
            str_word = line.strip()
    letter_list = []
    letter_list.append(str_word[0])
    temp_letter = str_word[0]
    count_list = []
    count = 0
    i = 0
    while i < len(str_word):
        if temp_letter == str_word[i]:
            count += 1
            i += 1
        else:
            letter_list.append(str_word[i])
            count_list.append(count)
            temp_letter = str_word[i]
            count = 0
    count_list.append(count)
    combination = [str(i)+e for i, e in zip(count_list, letter_list)]
    print(''.join(combination))

    with open('HW_5\Out_data_without_spaces.txt', 'a') as file:
        file.write(f'{"".join(combination)}\n')


l = str_list_without_space(10)
write_file_without_spaces(l)
letter_count('HW_5\In_data_without_spaces.txt')
