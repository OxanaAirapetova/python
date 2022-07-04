# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
#
# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps

def val_checker(deco_param):
    def wrapper(my_func):
        @wraps(my_func)
        def tag_wrapper(arg):
            if deco_param(arg) == True:
                qwe = my_func(arg)
                print(qwe)
            else:
                raise ValueError(arg)


        return tag_wrapper
    return wrapper



@val_checker(lambda num: num > 0)
def calc_cube(num):
    return num ** 5
result = calc_cube(6)
print(calc_cube.__name__)