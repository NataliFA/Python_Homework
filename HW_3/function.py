from random import randint
from random import uniform

# список целых чисел
def int_list_creation(n: int):
    lst_numbers = []
    for i in range(0, n):
        lst_numbers.append(randint(1, 11))
    return lst_numbers

# список вещественных чисел, 2 знака после запятой
def float_list_creation(n: int):
    lst_numbers = []
    for i in range(0, n):
        lst_numbers.append(round(uniform(1.5, 11.5),2))
    return lst_numbers

# преобразование списка целых чисел в список строк
def int_num_in_str(data: list):
    string_list = []
    for i in data:
        string_list.append(str(i))
    return string_list
