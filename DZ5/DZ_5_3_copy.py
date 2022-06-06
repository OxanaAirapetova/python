# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше
# элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать,
# # в каких ситуациях генератор даст эффект.

from itertools import zip_longest

# Решение по заданию
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
delta = len(klasses) - len(tutors)
final = klasses[-int(delta):]
gen_final = (raw for raw in final)
gen = ((i, j) for i, j in zip(tutors, klasses))

print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))
print(next(gen, (None, next((raw for raw in klasses[-int(delta):])))))


# Решение для читеров
print(tuple(zip_longest(['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'],
                        ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'], fillvalue=None)))
