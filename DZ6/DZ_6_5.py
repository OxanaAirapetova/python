# ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
import json
import psutil
import os
import sys
from itertools import zip_longest
argv = sys.argv[1:]
user_cmd, hobby_cmd, uh = argv
users = open('../users.csv', encoding='UTF-8')
hobby = open('../hobby.csv', encoding='UTF-8')

user_list = list(k.strip() for k in users) #создаем списки из файлов, чтобы потом сравнивать их длину в условии
hobby_list = list(v.strip() for v in hobby)

users.close()
hobby.close()

users = open(user_cmd, encoding='UTF-8')
print(f'Искомый список пользователей:\n{users.read()}\n')

hobby = open(hobby_cmd, encoding='UTF-8')
print(f'Искомый список дисциплин:\n{hobby.read()}\n')

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
    with open(uh, 'r+', encoding='UTF-8') as uh_cmd:
        for us, ho in zip_longest(u_list, h_list):
             if us is not None:
                 us = ''.join(us)
             if ho is not None:
                 ho = ' '.join(ho)
             enter = f'{us}: {ho}\n'
             uh_cmd.write(enter)
        print(f'Файл на выходе:\n{uh_cmd.read()}')
else:
    exit(1)

users.close()
hobby.close()