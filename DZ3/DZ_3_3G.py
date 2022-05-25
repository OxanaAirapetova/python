#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
#возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
#содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
#{
 #   "И": ["Иван", "Илья"],
 #   "М": ["Мария"], "П": ["Петр"]
#}

def thesaurus(*names):
    names_dictionary = {}

    for i in names:
        key = i[0]
        if key not in names_dictionary:
            names_dictionary[key] = []
        names_dictionary[key].append(i)
        # return print(names_dictionary) команда возвращения словаря
    for key, value in names_dictionary.items():
        print(f'"{key}":{value}')




thesaurus('Петя', 'Андрей', 'Петруха', 'Вася', 'Виталик', 'Алексей')