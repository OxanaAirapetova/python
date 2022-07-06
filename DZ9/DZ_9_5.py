# Реализовать класс Stationery (канцелярская принадлежность):
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'Уникальное сообщение {self.title} для класса Pen')
class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'Уникальное сообщение {self.title} для класса Pencil')
class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'Уникальное сообщение {self.title} для класса Handle')

stat_stat = Stationery('Канцелярия')
stat_stat.draw()
pen_pen = Pen('Ручка')
pen_pen.draw()
pencil_pencil = Pencil('Карандаш')
pencil_pencil.draw()
handle_handle = Handle('Маркер')
handle_handle.draw()