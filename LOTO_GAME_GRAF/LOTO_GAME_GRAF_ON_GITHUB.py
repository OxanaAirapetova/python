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
from tkinter import *
from tkinter import messagebox


class LotoCard:
    def __init__(self):
        self.args = ''
        self.args2 = ''

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
            self.args += f'{arr_sorted_final}\n'
        return self.args

    def card2(self):
        b = []

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
            self.args2 += f'{b_sorted_final}\n'
        return self.args2


class LotoGame:
    def __init__(self, player, computer, name_player, name_computer):
        self.player = player
        self.computer = computer
        self.name_player = name_player
        self.name_computer = name_computer

    def game(self):
        # # СОЗДАНИЕ ОКНА --------------------------------
        display = Tk()
        display.title('ЛОТО')
        display.geometry('700x700')
        display.configure(bg='lightgray')

        # ВВОД ИМЕНИ ----------------------------------------------
        hi = Label(display, text=f'Введите ваше имя', font='Arial 14', bg='lightgray')
        message = StringVar()
        hi_name = Entry(display, textvariable=message, width=30, bd=3)
        hi.place(relx=.5, rely=.4, anchor=CENTER)
        hi_name.place(relx=.5, rely=.45, anchor=CENTER)

        # КОЛЛЕКЦИЯ НУЖНЫХ КНОПОК--------------------------------------
        starter = Button(display, text='Далее к приветствию', bg='lightgray')
        starter_pick = Button(display, text='Далее', bg='lightgray')
        lets_go = Button(display, text='Начать игру', bg='lightgray')
        yes = Button(display, text=f'ДА')
        no = Button(display, text=f'НЕТ')

        # ВВОД КОМАНДЫ ДЛЯ КНОПКИ "НАЧАТЬ ИГРУ" И ВВОД КНОПКИ "НАЧАТЬ"---------------------

        result = Label(display, text=f'Здравствуйте,{message.get()}!\n'
                                     f'Вас приветствует игра Лото!',
                       font='Arial 14',
                       bg='lightgray')

        result_2 = Label(display, text=f'{hi_name.get()}Выберите уровень сложности',
                         font='Arial 12',
                         bg='lightgray')
        starter.place(relx=.5, rely=.52, anchor=CENTER)

        def name_name(ev):
            entry_name = message.get()
            name_lbl = Label(display, text=f'Здравствуйте,{entry_name}!\n'
                                         f'Вас приветствует игра Лото!',
                           font='Arial 14',
                           bg='lightgray')
            name_lbl.place(relx=.5, rely=.42, anchor=CENTER)
            hi.destroy()
            starter.destroy()
            starter_pick.place(relx=.5, rely=.5, anchor=CENTER)
            hi_name.destroy()
            starter_pick.bind('<Button-1>', lambda x: (name_lbl.destroy(),
                                                       regulations_frame.pack(), regulations.pack(),
                                                       starter_pick.destroy(),
                                                       difficult_fr.place(relx=.5, rely=.4, anchor=CENTER),
                                                       easy.pack(),
                                                       medium.pack(),
                                                       hard.pack(),
                                                       lets_go.place(relx=.5, rely=.55, anchor=CENTER)))

        # ВВОД УРОВНЯ СЛОЖНОСТИ---------------------------------------------------------
        difficult_fr = LabelFrame(text='ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ', bg='lightgray')
        var = IntVar()
        var.set(0)
        easy = Radiobutton(difficult_fr, text='Легкий', variable=var, value=0, bg='green')
        medium = Radiobutton(difficult_fr, text='Средний', variable=var, value=1, bg='yellow')
        hard = Radiobutton(difficult_fr, text='Тяжёлый', variable=var, value=2, bg='red')
        # ПРАВИЛА ИГРЫ--------------------------------------------------------------------
        regulations_frame = LabelFrame(text='Правила игры', bg='red')
        regulations = Label(regulations_frame, text='Есть 90 бочонков с номерами от 1 до 90.\n '
                                                    'Каждый ход выпадает один бочонок со случайной цифрой.\n '
                                                    'Вам необходимо проверять, есть ли эта цифра'
                                                    ' в вашей карточке\n. Если ДА, то вы нажимаете '
                                                    'соответствующую кнопку, '
                                                    'и она зачеркивается.\n'
                                                    'Если цифры НЕТ, то вы нажимаете соответствующую кнопку, '
                                                    'и игра продолжается.\n '
                                                    'Проиграть вы можете в двух случаях:\n 1) если цифра'
                                                    'на карточке есть, но вы ее не увидите и нажмете НЕТ\n '
                                                    '2) если цифры на карточке нет,'
                                                    ' а вы нажмете ДА. \n'
                                                    'Вероятность такой ошибки у компьютера зависит от уровня сложности, '
                                                    'который вы выберете\n'
                                                    'Хорошей игры!:)', font='Arial 10', bg='lightyellow')
        starter.bind('<Button-1>', name_name)
        # СОЗДАНИЕ ФРЕЙМОВ----------------------------------------------
        self.f_rgt = LabelFrame(text=f'{self.name_computer}', bg='red')
        self.f_lft = LabelFrame(text=f'{self.name_player}', bg='green')
        user_card_lbl = Label(self.f_lft, text=f'{self.player}', bg='lightyellow')
        computer_card_lbl = Label(self.f_rgt, text=f'{self.computer}', bg='lightyellow')
        # РАЗМЕЩЕНИЕ КАРТОЧЕК--------------------------------------------

        player_re = re.findall('\d+', self.player)
        computer_re = re.findall('\d+', self.computer)
        self.player_re_one_list = [elem_user for elem_user in player_re]
        self.computer_re_one_list = [elem_comp for elem_comp in computer_re]

        def lets(ev):
            self.f_lft.place(relx=.35, rely=.1, anchor=CENTER)
            self.f_rgt.place(relx=.65, rely=.1, anchor=CENTER)
            user_card_lbl.pack()
            computer_card_lbl.pack()
            easy.destroy()
            medium.destroy()
            hard.destroy()
            starter_pick.destroy()
            lets_go.destroy()
            result_2.destroy()
            difficult_fr.destroy()
            regulations_frame.destroy()
            self.kegs = list(range(1, 91))

            def barrelfunc():

                self.barrel = self.kegs.pop(self.kegs.index(random.choice(self.kegs)))

                self.result = Label(display,
                                    text=f'Вам выпал бочонок №{self.barrel}! Осталось {len(self.kegs)} шт.\n'
                                         f'Зачеркнуть эту цифру на карточке?\n', bg='lightgray')
                self.result.place(relx=.5, rely=.25, anchor=CENTER)

                def yes_click(ev):
                    if str(self.barrel) in self.player_re_one_list:
                        self.f_lft.destroy()
                        self.f_lft = LabelFrame(text=f'{self.name_player}', bg='green')
                        self.f_lft.place(relx=.35, rely=.1, anchor=CENTER)
                        self.player_re_one_list = ['-' if number == str(self.barrel) else
                                                   number for number in self.player_re_one_list]
                        self.player_re_one_list_final = '\n'.join([' '.join(j)
                                                                   for j in [list(i) for i in
                                                                             np.reshape(self.player_re_one_list,
                                                                                        (3, 5))]])
                        self.card_user_vis = Label(self.f_lft, text=f'{self.player_re_one_list_final}',
                                                   bg='lightyellow')
                        self.card_user_vis.pack()

                        def dif_l(dl):
                            lvl_rnd = random.random()
                            if lvl_rnd >= dl:
                                self.f_rgt.destroy()
                                self.f_rgt = LabelFrame(text=f'{self.name_computer}', bg='red')
                                self.f_rgt.place(relx=.65, rely=.1, anchor=CENTER)
                                self.computer_re_one_list = ['-' if number == str(self.barrel) else
                                                             number for number in self.computer_re_one_list]
                                self.computer_re_one_list_final = '\n'.join([' '.join(j)
                                                                             for j in [list(i) for i in
                                                                                       np.reshape(
                                                                                           self.computer_re_one_list,
                                                                                           (3, 5))]])
                                self.card_comp_vis = Label(self.f_rgt, text=f'{self.computer_re_one_list_final}',
                                                           bg='lightyellow')
                                self.card_comp_vis.pack()
                            else:
                                Label(display, text='КОМПЬЮТЕР ОШИБСЯ!(после нажатия да) ВЫ ВЫИГРАЛИ').pack()

                        if var.get() == 0:
                            dif_l(0.05)
                        elif var.get() == 1:
                            dif_l(0.02)
                        elif var.get() == 2:
                            dif_l(0)
                        barrelfunc()
                    else:
                        def lose(lose_txt):
                            Label(display, text=lose_txt, font='Arial 20',
                                  bg='lightgray').place(relx=.5, rely=.3, anchor=CENTER)
                            self.f_lft.destroy()
                            self.f_rgt.destroy()
                            yes.destroy()
                            no.destroy()
                            self.result.destroy()
                            result_2.destroy()
                            ex = Button(display, text='ВЫЙТИ', height=2, width=7, font='Arial 18',
                                        command=lambda: display.quit())
                            ex.place(relx=.5, rely=.5, anchor=CENTER)

                        lose('Цифры нет на карточке! Вы проиграли!')

                def no_click(ev):
                    if str(self.barrel) in self.player_re_one_list:
                        Label(display, text='Цифра есть на карточке! Вы проиграли!', font='Arial 20',
                              bg='lightgray').place(relx=.5, rely=.3, anchor=CENTER)
                        self.f_lft.destroy()
                        self.f_rgt.destroy()
                        yes.destroy()
                        no.destroy()
                        self.result.destroy()
                        result_2.destroy()
                        ex = Button(display, text='ВЫЙТИ', height=2, width=7, font='Arial 18',
                                    command=lambda: display.quit())
                        ex.place(relx=.5, rely=.5, anchor=CENTER)
                    else:
                        self.f_lft.destroy()
                        self.f_lft = LabelFrame(text=f'{self.name_player}', bg='green')
                        self.f_lft.place(relx=.35, rely=.1, anchor=CENTER)

                        self.player_re_one_list_final = '\n'.join([' '.join(j)
                                                                   for j in [list(i) for i in
                                                                             np.reshape(self.player_re_one_list,
                                                                                        (3, 5))]])
                        self.card_user_vis = Label(self.f_lft, text=f'{self.player_re_one_list_final}',
                                                   bg='lightyellow')
                        self.card_user_vis.pack()

                        def dif_l(dl):
                            lvl_rnd = random.random()
                            if lvl_rnd > dl:
                                self.f_rgt.destroy()
                                self.f_rgt = LabelFrame(text=f'{self.name_computer}', bg='red')
                                self.f_rgt.place(relx=.65, rely=.1, anchor=CENTER)
                                self.computer_re_one_list = ['-' if number == str(self.barrel) else
                                                             number for number in self.computer_re_one_list]
                                self.computer_re_one_list_final = '\n'.join([' '.join(j)
                                                                             for j in [list(i) for i in
                                                                                       np.reshape(
                                                                                           self.computer_re_one_list,
                                                                                           (3, 5))]])
                                self.card_comp_vis = Label(self.f_rgt, text=f'{self.computer_re_one_list_final}',
                                                           bg='lightyellow')
                                self.card_comp_vis.pack()
                            else:
                                Label(display, text='КОМПЬЮТЕР ОШИБСЯ!(после нажатия НЕТ) ВЫ ВЫИГРАЛИ').pack()

                        if var.get() == 0:
                            dif_l(0)
                        elif var.get() == 1:
                            dif_l(0)
                        elif var.get() == 2:
                            dif_l(0)
                        barrelfunc()

                yes.bind('<Button-1>', yes_click)
                no.bind('<Button-1>', no_click)
                yes.place(relx=.45, rely=.35, anchor=CENTER)
                no.place(relx=.55, rely=.35, anchor=CENTER)
                if self.player_re_one_list.count('-') == 15 or self.computer_re_one_list.count('-') == 15:
                    def win(pl, num, win_name):
                        if pl.count('-') == num:
                            ms = messagebox.showinfo('Конец игры', win_name)
                            if ms == 'OK':
                                display.destroy()

                    win(self.player_re_one_list, 15, 'Все цифры зачеркнуты! Вы выиграли!')
                    win(self.computer_re_one_list, 15, 'Компьютер выиграл!')
                    return

            barrelfunc()

        lets_go.bind('<Button-1>', lets)
        display.mainloop()


a = LotoCard()
b = LotoCard()
my_name = 'Yanissss'
qwe = LotoGame(a.card(), a.card2(), my_name, 'Компьютер')
qwe.game()
