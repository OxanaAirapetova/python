# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
    # |--settings
    # |--mainapp
    # |--adminapp
    # |--authapp
import os
#простой способ через переход в нужную директорию и создание папок
try:
    os.mkdir(os.path.join('my_project'))
    os.chdir('my_project')
    os.mkdir(os.path.join('settings'))
    os.mkdir(os.path.join('mainapp'))
    os.mkdir(os.path.join('adminapp'))
    os.mkdir(os.path.join('authapp'))
except FileExistsError:
    print('Одна из папок уже существует')

#способ через словарь
directory = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
try:
    for key, val in directory.items():
        for i in val:
            os.makedirs(os.path.join(key, i))
except FileExistsError:
    print('Одна из папок уже существует')



