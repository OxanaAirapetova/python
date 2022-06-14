# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них
# словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много
# раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
from itertools import zip_longest
import json

users = open('../users.csv', encoding='UTF-8')
hobby = open('../hobby.csv', encoding='UTF-8')

key_list = list(k.strip() for k in users)
val_list = list(v.strip() for v in hobby)

if len(val_list) <= len(key_list):
    users_hobby = {key: val for key, val in zip_longest(key_list, val_list)}
    print(users_hobby)
    with open('../dict_name_hobby.json', 'w', encoding='UTF-8') as d:
        json.dump(users_hobby, d, ensure_ascii=False)
else:
    exit(1)

users.close()
hobby.close()
