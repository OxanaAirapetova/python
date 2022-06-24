# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import os
import yaml
first_directory = {'my_project':
                       [{'settings':
                             ['__init__.py',
                              'dev.py',
                              'prod.py']},
                        {'mainapp':
                             ['__init__.py',
                              'models.py',
                              'view.py',
                              {'templates':
                                   {'mainapp':
                                        ['base.html',
                                         'index.html']}}]},
                        {'authapp':
                             ['__init__.py',
                              'models.py',
                              'view.py',
                              {'templates':
                                   {'authapp':
                                        ['base.html',
                                         'index.html']}}]}]}

try:
    for key, val in first_directory.items():
        os.mkdir(os.path.join(key))
        os.chdir(os.path.join(key))
        for item1 in val:
            for key2, val2 in item1.items():
                os.mkdir(os.path.join(key2))
                os.chdir(os.path.join(key2))
                for item2 in val2:
                    if item2 == str(item2):
                        open(item2, 'w')
                    elif item2 == dict(item2):
                        item2_dict = dict(item2)
                        for key3, val3 in item2_dict.items():
                            os.chdir(os.path.join('..'))
                            os.mkdir(os.path.join(key3))
                            os.chdir(os.path.join(key3))############ templates
                            for key4, val4 in val3.items():
                                os.mkdir(os.path.join(key4))
                                os.chdir(os.path.join(key4))
                                for item3 in val4:
                                    open(item3, 'w')

except FileExistsError:
    print('Такие папки уже существуют')