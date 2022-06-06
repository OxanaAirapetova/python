# * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


# Вариант для вывода на экран

num = int(input('Введите любое число: '))
generic_nums_hard = (elem for elem in range(1, num + 1, 2))
for i in generic_nums_hard:
    print(i)
print(type(generic_nums_hard))

# Вариант для консоли

num_console = int(input('Введите любое число: '))
generic_nums_hard_console = (item for item in range(1, num_console + 1, 2))
next(generic_nums_hard_console)
