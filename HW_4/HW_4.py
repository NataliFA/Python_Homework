# 1. Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример: при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

num = float(input('До какого знака после запятой округлить число пи? '))


def pi_calculation(d):  # Нилакант
    res = 0
    if 0 < d < 1:
        count = 0
        while d != int(d):
            d *= 10
            count += 1
        d = count

    for i in range(2, 10000, 4):
        num1 = 4/(i*(i+1)*(i+2))
        num2 = 4/((i+2)*(i+3)*(i+4))
        res = res + (num1 - num2)
    pi = 3 + res
    return round(pi, int(d))


print(pi_calculation(num))


# 2.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Посмотрели, что такое множество? Вот здесь его не используйте.

lst_num = [5, 10, 15, 2, 2, 5, 1, 2, 3, 6, 8, 15, ]


def non_repeating_numbers(lst: list):
    lst.sort()
    rep_list = []
    for i in range(0, len(lst)-1, 1):
        if lst[i] == lst[i+1]:
            rep_list.append(lst[i])
    for el in rep_list:
        while el in lst:
            lst.remove(el)
    return lst


print(non_repeating_numbers(lst_num))


# 3. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

num = int(input('Enter number: '))


def multipliers(n):
    mult_num = set()
    for x in range(2, n+1):
        while n != 1:
            if n % x == 0:
                mult_num.add(x)
                n //= x
            else:
                x += 1
    return mult_num


print(f'Простые множители числа {num} -> {multipliers(num)}')

# # 4. В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# # В файле содержится, например:
# # Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

str_sentence = 'Мама сшила м0не штаны и7з бере9зовой кор45ы 893.'


def text_in_file(s: str):
    with open('HW_4/Text_file.txt', 'w', encoding='utf-8') as t_file:
        t_file.write(s)


def find_number(file_name):
    w = []
    with open(file_name, 'r', encoding='utf-8') as data:
        w = data.read()

    text = w.split()
    num_in_word = []

    for el in text:
        for letter in el:
            if letter.isdigit():
                num_in_word.append(el)
                break

    for i in num_in_word:
        text.remove(i)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(' '.join(text))
        file.write('.')

    return text


text_in_file(str_sentence)
path = 'HW_4\Text_file.txt'
print(f'{" ".join(find_number(path))}.')
