# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

import json
import psutil
import os
from itertools import zip_longest

users = open('../users.csv', 'r', encoding='UTF-8')
hobby = open('../hobby.csv', encoding='UTF-8')

user_list = list(k.strip() for k in users) #создаем списки из файлов, чтобы потом сравнивать их длину в условии
hobby_list = list(v.strip() for v in hobby)

users.close()
hobby.close()

users = open('../users.csv', 'r', encoding='UTF-8')
hobby = open('../hobby.csv', encoding='UTF-8')

size_users = os.path.getsize('../users.csv')  # размер файла users: 692 байт
size_hobby = os.path.getsize('../hobby.csv')  # размер файла hobby: 263 байт
asus_rog_ram = psutil.virtual_memory()[0]  # истинный размер ОЗУ: 16559521792 байт
# Возьмем выдуманное значение оперативной памяти равное 200 байтам
ram_fake = 200
if len(hobby_list) < len(user_list):
    u_list = []
    h_list = []
    while users.tell() < ram_fake:
        line_u = users.readline().split()
        u_list.append(line_u)
    while hobby.tell() < ram_fake:
        line_h = hobby.readline().split()
        h_list.append(line_h)
    with open('../users_hobby.txt', 'r+', encoding='UTF-8') as uh:
        for us, ho in zip_longest(u_list, h_list):
            if us is not None:
                us = ''.join(us)
            if ho is not None:
                ho = ' '.join(ho)
            enter = f'{us}: {ho}\n'
            uh.write(enter)
             #для проверки

else:
    exit(1)

users.close()
hobby.close()