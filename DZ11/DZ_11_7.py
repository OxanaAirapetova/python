# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
# число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
# выполнить сложение и умножение созданных экземпляров. Проверить корректность
# полученного результата.

#Оптимальный способ
class ComplexNumber:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return (self.num + other.num)
    def __mul__(self, other):
        return self.num * other.num
print(f'Сложение:')
complex_num_1 = ComplexNumber(complex(5, 6))
complex_num_2 = ComplexNumber(complex(1, 2))
print(complex_num_1 + complex_num_2)
print(f'Умножение: ')
complex_num_1 = ComplexNumber(complex(3, 7))
complex_num_2 = ComplexNumber(complex(7, 9))
print(complex_num_1 * complex_num_2)

#Неудобный способ
class NumberComplex:
    def __init__(self, realpart, fakepart, *i):
        self.realpart = realpart
        self.fakepart = fakepart
    def __add__(self, other):
        return f'{self.realpart + other.realpart} + {self.fakepart + other.fakepart}i'
    def __mul__(self, other):
        rr = self.realpart * other.realpart
        rf = self.realpart * other.fakepart
        fr = self.fakepart * other.realpart
        ff = self.fakepart * other.fakepart
        return f'{rr - ff} + {rf + fr}i'
print(f'Второе сложение: ')
complex_num_1 = NumberComplex(5, 6)
complex_num_2 = NumberComplex(1, 2)
print(complex_num_1 + complex_num_2)
print(f'Второе умножение: ')
complex_num_1 = NumberComplex(3, 7)
complex_num_2 = NumberComplex(7, 9)
print(complex_num_1 * complex_num_2)