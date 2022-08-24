# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


"""1 способ"""

try:
    class Zerozero:
        def __init__(self, num_user):
            self.num_user = num_user
        def __truediv__(self, other):
            return f'Первое частное: {self.num_user / other.num_user}'
    z = Zerozero(int(input('Введите делимое (первый код): ')))
    z2 = Zerozero(int(input('Введите делитель (первый код): ')))
    print(z / z2)
except ZeroDivisionError:
    print(f'Деление на ноль в первом коде! Ошибка!')

"""2 способ"""

class ZeroError:
    def __init__(self, divident, divider):
        self.divident = divident
        self.divider = divider
    @staticmethod
    def division_operation(divident, divider):
        try:
            result = divident / divider
            return f'Второе частное {result}'
        except ZeroDivisionError:
            return f'Деление на ноль во втором коде! Ошибка!'
divident_input = int(input('Введите делимое (второй код): '))
divider_input = int(input('Введите делитель (второй код): '))
print(ZeroError.division_operation(divident_input, divider_input))
