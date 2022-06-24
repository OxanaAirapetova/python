# * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import json
import os
from os.path import getsize, join
from itertools import zip_longest

os.chdir(os.path.join('testcola'))

size_arr = []  # начальный список размеров файлов
name_arr = []  # начальный список имен файлов

for r, d, f in os.walk('.'):
    total_size = list(getsize(join(r, name_file)) for name_file in f)
    size_arr.append(total_size)
    name_arr.append(f)

size_arr_full = list(j for i in size_arr for j in i)  # превращение в единый список размеров
name_arr_full = list(j for i in name_arr for j in i)  # превращение в единый список имен

file_format = list(os.path.splitext(i) for i in name_arr_full)  # отсечение формата файла в списке имен и получение списка кортеже (имя, формат)
ext_file = list(i[1] for i in file_format)  # создание единого списка форматов файлов

big_files_tuples = list(zip_longest(size_arr_full, ext_file))  # склеивание единого списка размеров и единого списка форматов
big_files_list = list(list(i) for i in big_files_tuples)  # превращение всего этого из списка кортежей в список списков


def file_system(b):
    dict_dir = {}
    for _ in big_files_list:
        if b == 100:
            final_size_list_first = [item for item in big_files_list if item[0] <= 100]
            final_ext_list_first = list(set(elem[1] for elem in final_size_list_first))
            dict_dir.setdefault(b, (len(final_size_list_first), final_ext_list_first))
        b *= 10
        if b <= 10000000:
            final_size_list_second = [item for item in big_files_list if b / 10 < item[0] <= b]
            final_ext_list_second = list(set(elem[1] for elem in final_size_list_second))
            dict_dir.setdefault(b, (len(final_size_list_second), final_ext_list_second))
    for key, val in dict_dir.items():
        print(f'{key} байт: {val} ')

    with open('testcola_summary.json', 'w', encoding='UTF-8') as testcola_json:
        json.dump(dict_dir, testcola_json, ensure_ascii=False)

file_system(100)