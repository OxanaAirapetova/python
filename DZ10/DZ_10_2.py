# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
# знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
# декоратора @property.
from abc import ABC, abstractmethod

class clother:
    def __init__(self, par):
        self.par = par
    @abstractmethod
    def full(self):
        pass
class Coat(clother):
    @property
    def full(self):
        return ((self.par / 6.5) + 0.5)
class Costume(clother):
    @property
    def full(self):
        return ((2 * self.par) + 0.3)

coat = Coat(40)
costume = Costume(165)
print(round(coat.full, 2))
print(round(costume.full, 2))







# class MyClass:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#     @property
#     def my_method(self):
#         return f'{self.param_1}, {self.param_2}'
# mc = MyClass("text_1", "text_2")
# print(mc.param_1)
# print(mc.param_2)
# print(mc.my_method)
