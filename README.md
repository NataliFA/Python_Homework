## Домашняя работа по изучению Python
___
1.  ДЗ_1 

* Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 

* Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

* Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

* Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

* Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. *Пример:* A (3,6); B (2,1) -> 5,09
___
2.  ДЗ_2

* Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. *Пример:* 0,56 -> 11

* Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. *Пример:* пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

* Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму . *Пример:* Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

* Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
не использовать random.randint и вообще библиотеку random. Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности.
___
3.  ДЗ_3

* Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. *Пример:*  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12.

* Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. *Пример:* [2, 3, 4, 5, 6] => [12, 15, 16]; (4 возвести в квадрат)

* Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. *Пример:* [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

* Напишите программу, которая будет преобразовывать десятичное число в двоичное. *Пример:* 45 -> 101101

* Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. *Пример:* для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

___
4.  ДЗ_4

* Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
*Пример:* при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

* Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
Посмотрели, что такое множество? Вот здесь его не используйте.

* Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
*Пример:* при N = 12 -> [2, 3]

* В текстовом файле удалить все слова, которые содержат хотя бы одну цифру. 
*В файле содержится, например:*
Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
[Это](https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699) на случай возникновения непонятных символов в файле.
___
5.  ДЗ_5

* Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
*Пример:*'абвгдейка - это передача' = >" - это передача"

* Создайте программу для игры с конфетами человек против человека.
*Условие задачи:* На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

    a) Добавьте игру против бота

    b) Подумайте как наделить бота ""интеллектом""

* Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.

    *Пример:*
    ['python', 'c#']
    [1,2]
    
    Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. [(1,'PYTHON'), (2,'C#')]
    
    Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
    [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет] [(1,'PYTHON'), (102,'C#')]

    Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой [таблице](https://www.charset.org/utf-8), в третьем столбце:
    
    Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком.

* Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
___
6.  ДЗ_6

* С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce:
    1. Определить, присутствует ли в заданном списке строк, некоторое число
    2. Найти сумму чисел списка стоящих на нечетной позиции
    3. Найти расстояние между двумя точками пространства(числа вводятся через пробел)
    4. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

        **Примеры:**
        - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
        - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
        - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
  
        - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1 

    5. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    6. Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
---
_Полезная информация) Допустим, у вас есть функция:_

    def is_int(input_number:str):
    '''
    Проверяет аргумент на принадлежность к int
    params:input_number - введенное значение
    return: int или False
    '''
    try:
        input_number = int(input_number)
        return input_number
    except ValueError:
        return False
_Вы можете использовать эту функцию в лямбде. Делается это, примерно, вот так:_

    lambda input_number: is_int(input_number)

или даже необязательно называть это input_number: 
    
    lambda char: is_int(char)_



