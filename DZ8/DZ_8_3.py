# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции,
# например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
# """

from functools import wraps

def type_logger(func):

    @wraps(func)
    def wrapper_logger(arg1, arg2, arg3):
        return f'1-й параметр функции {func.__name__}: {arg1}, тип {type(arg1)}, ' \
               f'\n2-й параметр функции {func.__name__}: {arg2}, тип {type(arg2)}, ' \
               f'\n3-й параметр функции {func.__name__}: {arg3}, тип {type(arg3)}'
    return wrapper_logger

@type_logger
def calc_cube(int1, int2, flt1):
    return int1 ** 3, int2 ** 2, flt1*10


function = calc_cube(3, 6, 2.5)
print(function)

print(calc_cube.__name__)
print(calc_cube.__doc__)