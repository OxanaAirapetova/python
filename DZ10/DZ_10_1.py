# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, list):
        self.list = list
    def __str__(self):
        return '\n'.join([' '.join(map(lambda x: str(x), idx)) for idx in self.list])
    def __add__(self, other):
        result = []
        final_result = ''
        if len(self.list) == len(other.list):
            for i, j in zip(self.list, other.list):
                if len(i) == len(j):
                    result.append([i_small + j_small for i_small, j_small in zip(i, j)])
        for item in result:
            final_result += ' '.join(map(str, item)) + '\n'
        return final_result

matrix_1 = Matrix([[1, 2], [3, 4], [1000, 2000]])
matrix_2 = Matrix([[10, 12], [14, 15], [2314, 10321]])
print(f'Первая матрица\n{matrix_1}')
print(f'Вторая матрица\n{matrix_2}')
print(f'Сумма матриц\n{matrix_1 + matrix_2}')
