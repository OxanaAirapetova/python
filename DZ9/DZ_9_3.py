#  Реализовать базовый класс Worker (работник):
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def name_worker(self):
        get_full_name = f'{self.name} {self.surname}. Его профессия - {self.position}'
        get_total_income = dict(self._income)
        return f'Работника зовут {get_full_name}, ' \
               f'и он зарабатывает {sum(get_total_income.values())} руб в месяц!'



position_worker = Position('Вася', 'Петров', 'Строитель', {'wage': 40000,
                                                     'bonus': 10000})
position_worker.name_worker()

print(position_worker.name_worker())
