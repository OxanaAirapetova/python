# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
# {
# 100: 15,
# 1000: 3,
# 10000: 7,
# 100000: 2
# }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat

import os
from os.path import getsize, join

os.chdir(os.path.join('testcola'))
size_arr = []
file_names = []
dict_dir_1 = {}
for r, d, f in os.walk('.'):
    total_size = list(getsize(join(r, name_file)) for name_file in f)
    size_arr.append(total_size)
    file_names.append(f)
size_arr_full = list(j for i in size_arr for j in i)

#Способ "в лоб"
files_up_to_100 = sum(map(lambda x: x <= 100, size_arr_full))
files_up_to_1000 = sum(map(lambda x: 100 < x <= 1000, size_arr_full))
files_up_to_10000 = sum(map(lambda x: 1000 < x <= 10000, size_arr_full))
files_up_to_100000 = sum(map(lambda x: 10000 < x <= 100000, size_arr_full))
files_up_to_1000000 = sum(map(lambda x: 100000 < x <= 1000000, size_arr_full))
files_up_to_biggest = sum(map(lambda x: 1000000 < x, size_arr_full))

dict_dir_1.setdefault('100', files_up_to_100)
dict_dir_1.setdefault('1000', files_up_to_1000)
dict_dir_1.setdefault('10000', files_up_to_10000)
dict_dir_1.setdefault('100000', files_up_to_100000)
dict_dir_1.setdefault('1000000', files_up_to_1000000)
dict_dir_1.setdefault('1000000+', files_up_to_biggest)

for key, val in dict_dir_1.items():
    print(f'{key} байт: {val} файлов')
print('\n')


#Оптимизированный способ
def my_func(b):
    global files_up_to_100
    dict_dir = {}
    for _ in size_arr_full:
        if b == 100:
            files_up_to_100 = sum(map(lambda x: x <= b, size_arr_full))
            dict_dir.setdefault(b, files_up_to_100)
        b *= 10
        if b <= 10000000:
            files_up_to_ = sum(map(lambda x: b/10 < x <= b, size_arr_full))
            dict_dir.setdefault(b, files_up_to_)
    for key, val in dict_dir.items():
        print(f'{key} байт: {val}')
my_func(100)