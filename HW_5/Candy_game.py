# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
import random
import os
import time


def give_number():
    while True:
        num = input('Твой выбор: ')
        if num.lower() == 'exit':
            print('До встречи!')
            exit()
        try:
            while int(num) > 28 or int(num) < 1:
                print('Правила гласят: ты можешь взять не менее 1 и не более 28 конфет!')
                num = input('Твой выбор: ')
                if 1 <= int(num) < 29:
                    return int(num)
            return int(num)
        except ValueError:
            print('Необходимо ввести число!\n\
                Если же ты хочешь закончить игру, напиши "exit"')


def clear_screen():
    time.sleep(0.5)
    os.system('cls')


def player_turn(candies):
    clear_screen()
    print(f'\nНа столе лежит {candies} конфет\n')
    turn = give_number()
    while turn >= candies:
        print(f'Вы не можете взять более {candies} конфет')
        turn = give_number()
    return turn


def bot_turn(complication, candies):
    if complication == 1:
        bot_turn = random.randint(1, 28)
        if bot_turn > candies:
            bot_turn = random.randint(1, candies-1)
        print(f'\nБот берет со стола {bot_turn} конфет')
        time.sleep(0.9)
        return bot_turn
    else:
        if candies == 29:
            bot_turn = 28
        elif candies <= 28:
            bot_turn = candies - 1
        elif candies % 29 == 0:
            bot_turn = 27
        else:
            bot_turn = candies % 29
        print(f'\nКоварный умный бот берет со стола {bot_turn} конфет')
        time.sleep(0.9)
        return bot_turn


def two_players(all_candies):
    player_1 = input('Игрок № 1, напишите Ваше имя: ')
    player_2 = input('Игрок № 2, как Вас зовут?: ')

    lottery = random.choice([1, 2])

    while all_candies != 1:
        if lottery == 1:
            print(
                '\033[32m'f'{player_1}, сколько конфет Вы возьмете?''\033[0m', end='  ')
            all_candies -= player_turn(all_candies)
            lottery = 2
        else:
            print(
                '\033[33m'f'{player_2}, сколько конфет Вы возьмете?''\033[0m', end='  ')
            all_candies -= player_turn(all_candies)
            lottery = 1

    if lottery == 1:
        victory(1, 1, player_2)
    else:
        victory(1, 2, player_1)


def player_and_bot1(all_candies):
    player = input('Представьтесь, пожалуйста:  ')

    lottery = random.choice([1, 2])

    while all_candies != 1:
        if lottery == 1:
            print(
                '\033[35m'f'{player}, сколько конфет Вы возьмете?''\033[0m', end=' ')
            all_candies -= player_turn(all_candies)
            lottery = 2
        else:
            all_candies -= bot_turn(1, all_candies)
            lottery = 1

    victory(2, lottery, player)


def player_and_bot2(all_candies):
    player = input('Хочу услышать звучание Вашего прекрасного имени:  ')

    lottery = random.choice([1, 2])

    while all_candies != 1:
        if lottery == 1:
            print(
                '\033[37m'f'{player}, сколько конфет Вы возьмете?''\033[0m', end=' ')
            all_candies -= player_turn(all_candies)
            lottery = 2
        else:
            all_candies -= bot_turn(2, all_candies)
            lottery = 1

    victory(2, lottery, player)


def start_game():
    number = give_number()
    с = 200
    if number == 1:
        two_players(с)
    elif number == 2:
        player_and_bot1(с)
    elif number == 3:
        player_and_bot2(с)
    else:
        print('Выбери режим 1, 2 или 3.')
        start_game()


def victory(game_mode, lot, player_name):
    if game_mode == 1:
        print('\033[33m'f'Поздравляю, {player_name}, Вы победили!''\033[0m')
    elif game_mode == 2 or game_mode == 3:
        if lot == 1:
            print(
                '\033[33m'f'Cегодня компьютер оказался умнее Вас! Удачи в следующий раз!''\033[0m')
        else:
            print(
                '\033[32m'f'Поздравляю, {player_name}, Вы победили!''\033[0m')


print('\n\
        Привет дорогой друг! Это Candy_game!\n\
    Перед игроками лежит 2021 конфета. Каждый по очереди берет от 1 до 28 конфет.\n\
    Проиграет тот, кто заберет последнюю конфету. Удачи!\n\
        \n\
    Выбери режим игры:\n\
        1. Игра против друга\n\
        2. Игра против бота\n\
        3. Игра против бота, наделённого интеллектом')

start_game()
