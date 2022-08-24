# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.
import re
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    def test(self):
        return f'Сегодня: {self.day_month_year}. Работает метод test'
    @classmethod
    def craft_integer(cls, day_month_year_cls):
        cls.day_month_year_cm = day_month_year_cls
        data_reg = re.findall(r'\d+', day_month_year_cls)
        data_integer = [int(idx) for idx in data_reg]
        return f'Вывод в методе с декоратором @classmethod:\n{data_integer}'
    @staticmethod
    def valid_data(day_month_year_stat):
        data_reg_2 = re.findall(r'\d+', day_month_year_stat)
        data_integer_2 = [int(idx2) for idx2 in data_reg_2]
        for _ in data_integer_2:
            print(f'Вывод в методе с декоратором @staticmethod:')
            if 0 < data_integer_2[0] <= 31:
                print(f'Такое число может существовать')
            else:
                print(f'Такого дня не существует')
            if 0 < data_integer_2[1] <= 12:
                print(f'Такой месяц существует')
            else:
                print(f'Несуществующий месяц')
            if 0 < data_integer_2[2] <= 2022:
                print(f'Такой год был или есть')
            else:
                print(f'Такой год еще не наступил или не входит в диапазон')
            break


print(Data.craft_integer('16-07-2022'))
Data.valid_data('30-07-2022')
"""РЕШЕНО"""