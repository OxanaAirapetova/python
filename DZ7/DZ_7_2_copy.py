# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
# текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации,
# библиотеки использовать нельзя.
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

f = open('config.yaml', 'w')
f.write(yaml.dump(first_directory))
f.close()

new_f = open('config.yaml')
first_directory = yaml.safe_load(new_f)
new_f.close()

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
                            os.mkdir(os.path.join(key3))
                            os.chdir(os.path.join(key3))
                            for key4, val4 in val3.items():
                                os.mkdir(os.path.join(key4))
                                os.chdir(os.path.join(key4))
                                for item3 in val4:
                                    open(item3, 'w')
                                os.chdir(os.path.join('..'))
                                os.chdir(os.path.join('..'))
                os.chdir(os.path.join('..'))

except FileExistsError:
    print('Такие папки уже существуют')
