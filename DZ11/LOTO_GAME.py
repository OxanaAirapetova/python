# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# —----------------------—
# 9 43 62 74 90
# 2 27 75 78 82
# 41 56 63 76 86
# —----------------------—
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# Если цифра есть на карточке - она зачеркивается и игра продолжается.
# Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# Если цифра есть на карточке - игрок проигрывает и игра завершается.
# Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# —--— Ваша карточка —-—
# 6 7 49 57 58
# 14 26 - 78 85
# 23 33 38 48 71
# —----------------------—
# — Карточка компьютера —-
# 7 87 - 14 11
# 16 49 55 88 77
# 15 20 - 76 -
# —----------------------—
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random
import numpy as np
import re


class LotoCard:
    def __init__(self):
        self.args = []
        self.args2 = []

    def card(self):
        arr = []
        while len(arr) < 27:
            rnd = random.randint(1, 90)
            if arr.count(rnd) < 1:
                arr.append(rnd)
        arr = sorted(arr, reverse=False)
        zero_s = [0] * 4
        arr_card = np.reshape(arr, (3, 9))
        for i in arr_card:
            idx_s = []
            while len(idx_s) <= 3:
                r_idx = random.randint(1, 8)
                if idx_s.count(r_idx) < 1:
                    idx_s.append(r_idx)
            i = np.array(i)
            i[idx_s] = zero_s
            arr_sorted_final = ' '.join(map(lambda x: str(x), ['' if idx == 0 else idx for idx in i]))
            self.args.append(f'\r{arr_sorted_final}\n')
        return self.args

    def card2(self):
        b = []
        self.args2 = []
        while len(b) < 27:
            rnd = random.randint(1, 90)
            if b.count(rnd) < 1:
                b.append(rnd)
        b = sorted(b, reverse=False)
        zero_x = [0] * 4
        b_card = np.reshape(b, (3, 9))
        for i in b_card:
            idx_s = []
            while len(idx_s) <= 3:
                r_idx = random.randint(1, 8)
                if idx_s.count(r_idx) < 1:
                    idx_s.append(r_idx)
            i = np.array(i)
            i[idx_s] = zero_x
            b_sorted_final = ' '.join(map(lambda x: str(x), ['' if idx == 0 else idx for idx in i]))
            self.args2.append(f'\r{b_sorted_final}\n')
        return self.args2


class LotoGame:
    def __init__(self, player, computer, name_player, name_computer):
        self.player = player
        self.computer = computer
        self.name_player = name_player
        self.name_computer = name_computer

    def game(self):
        print(f'Здравствуйте, {self.name_player}! Вас приветствует игра ЛОТО')
        difficulty_level = input('Выберите уровень сложности игры: e (easy), m (medium), h (hard) ')
        print(self.name_player)
        print(*self.player)
        print(self.name_computer)
        print(*self.computer)
        kegs = list(range(1, 91))
        player_re = [re.findall('\d+', i) for i in self.player]
        computer_re = [re.findall('\d+', i) for i in self.computer]
        player_re_one_list = [elem_user for item_user in player_re for elem_user in item_user]
        computer_re_one_list = [elem_comp for item_comp in computer_re for elem_comp in item_comp]

        def active_game(card_us, card_co):
            while card_us.count('-') < 15 or card_co.count('-') < 15:
                rnd = random.random()
                barrel = kegs.pop(kegs.index(random.choice(kegs)))
                result = input(f'Вам выпал бочонок №{barrel}! Осталось {len(kegs)} шт.\n'
                               f'Зачеркнуть эту цифру на карточке?\n'
                               f'Нажмите y/n')
                if result == 'y' or result == 'Y':
                    if str(barrel) in card_us:
                        card_us = ['-' if number == str(barrel) else number for number in card_us]
                        #                       num1_re_one_list_np = np.reshape(num1_re_one_list, (3, 5))
                        #               card = [list(i) for i in num1_re_one_list_np] оставлю на будущее
                        card_user_final = '\n'.join([' '.join(j)
                                                     for j in [list(i)
                                                               for i in np.reshape(card_us, (3, 5))]])
                        print(f'{self.name_player}\n{card_user_final}')

                        def dif_l(lvl, card_co=None):
                            if rnd > lvl:
                                card_co = ['-' if number == str(barrel) else number for number in card_co]
                                card_comp_final = '\n'.join([' '.join(j)
                                                             for j in [list(i)
                                                                       for i in np.reshape(card_co, (3, 5))]])
                                print(
                                    f'{self.name_computer}\n{card_comp_final}'
                                    f'\n---------------------------------------')
                            else:
                                print(f'{self.name_computer} ошибся! {self.name_player} выиграл!!')

                        if difficulty_level == 'e':
                            dif_l(0.04)
                        elif difficulty_level == 'm':
                            dif_l(0.03)
                        elif difficulty_level == 'h':
                            dif_l(0.01)
                        else:
                            print(f'Неправильный ввод')
                    else:
                        print(f'Цифры нет на карточке! Вы проиграли!')
                        break
                elif result == 'n' or result == 'N':
                    if str(barrel) in card_us:
                        print(f'Цифра есть на карточке! Вы проиграли')
                        break
                    else:
                        card_user_final = '\n'.join([' '.join(j)
                                                     for j in [list(i)
                                                               for i in np.reshape(card_us, (3, 5))]])
                        print(f'{self.name_player}\n{card_user_final}'
                              f'\n---------------------------------------')
                        ##########################################
                        if random.random() > 0.3:
                            card_co = ['-' if number == str(barrel) else number for number in card_co]
                            card_comp_final = '\n'.join([' '.join(j)
                                                         for j in [list(i)
                                                                   for i in np.reshape(card_co, (3, 5))]])
                            print(f'{self.name_computer}\n{card_comp_final}')
                        else:
                            print(f'{self.name_computer} ошибся! {self.name_player} выиграл rhffsdf!!')
                            break
                if card_us.count('-') == 15:
                    print(f'Игра окончена!{self.name_player} выиграл!')
                elif card_co.count('-') == 15:
                    print(f'Игра окончена! {self.name_computer} выиграл!')

        active_game(player_re_one_list, computer_re_one_list)


a = LotoCard()
b = LotoCard()
my_name = input('Ваше имя: ')
qwe = LotoGame(a.card(), a.card2(), my_name, 'Компьютер')
qwe.game()
