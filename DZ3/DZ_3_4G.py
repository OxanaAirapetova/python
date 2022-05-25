#* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с
# соответствующей буквы. Например:
#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
#{
 #   "А": {
 #       "П": ["Петр Алексеев"]
#    },
 #   "И": {
 #       "И": ["Илья Иванов"]
 #   },
  #  "С": {
  #      "И": ["Иван Сергеев", "Инна Серова"],
   #     "А": ["Анна Савельева"]
   # }
#}
#Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args):
    name_dictionary = {}
    for item in args:
        j = item.split()
        name, surname = j
        name_dictionary.setdefault(surname[0], {})
        name_dictionary[surname[0]].setdefault(name[0], [])
        name_dictionary[surname[0]][name[0]].append(item)

    for key, value in name_dictionary.items():
        print(f'"{key}":{value}')
    print(name_dictionary)
    #сортировка по ключам
    name_dictionary_keys = list(name_dictionary.keys())
    name_dictionary_keys.sort()
    print(name_dictionary_keys)



thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")