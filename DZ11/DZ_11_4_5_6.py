# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.

class Stock:
    def __init__(self):
        pass
    @classmethod
    def square(cls, l, s):
        cls.l = l
        cls.s = s
        square = l * s
        return f'Построили склад площадью {square} кв.м\n'
class OfficeEquipment:
    def __init__(self, color, barcode, manufacturer, country, amount):
        self.color = color
        self.barcode = barcode
        self.manufacturer = manufacturer
        self.country = country
        self.amount = amount
        self.acceptance = {'Цвет устройства': self.color,
                            'Штрих-код партии': self.barcode,
                                'Производитель': self.manufacturer,
                                    'Страна': self.country
                          }
        self.acceptance_read = '\n'.join([f'{k}: {v}'for k, v in self.acceptance.items()])
    def __str__(self):
        print(f'На склад пришли изделия в количестве {self.amount} шт')

class Printer(OfficeEquipment):
    def to_print(self, papers):
        self.papers = papers
        return f'После доставки было распечатано {papers} листов на устройстве {__class__.__name__} ' \
                f'с кодом {self.barcode} от производителя {self.manufacturer}\n'
    def __str__(self):
        super().__str__()
        return f'Это принтеры. Их характеристики:\n{self.acceptance_read}'
class Scan(OfficeEquipment):
    def to_scan(self, doc):
        self.doc = doc
        if self.country == 'США':
            return f'После доставки было отсканировано {self.doc} документов на устройстве {__class__.__name__} ' \
                    f'из {self.country}\n'
        else:
            return f'После доставки было отсканировано {self.doc} документов на устройстве {__class__.__name__} ' \
                    f'из {self.country}ии\n'
    def __str__(self):
        super().__str__()
        return f'Это сканеры. Их характеристики:\n{self.acceptance_read}'
class Xerox(OfficeEquipment):
    def to_xerox(self, copy):
        self.copy = copy
        return f'После доставки было скопировано {self.copy} бумаг на устройстве {__class__.__name__} ' \
                f'от {self.manufacturer}'
    def __str__(self):
        super().__str__()
        return f'Это ксероксы. Их характеристики:\n{self.acceptance_read}'
print(Stock.square(5, 6))
print(f'Отчёт по принтерам')

def report(result):
    while True:
        inpt_barcode = input('Введите штрихкод партии: ')
        if inpt_barcode.isdigit():
            inpt_barcode = int(inpt_barcode)
            break
        else:
            print(f'Ошибка! Штрихкод может состоять только из цифр!'
                  f' Введите данные заново')
            continue
    while True:
        inpt_country = input('Введите страну производителя: ')
        if inpt_country.isalpha():
            break
        else:
            print(f'Ошибка! Страна не может содержать цифры!')
            continue
    while True:
        inpt_amount = input('Введите количество устройств: ')
        if inpt_amount.isdigit():
            inpt_amount = int(inpt_amount)
        else:
            print(f'Ошибка! Количество устройств может состоять только из цифр!'
                  f' Введите данные заново')
            continue
        inpt_color = input('Введите цвет устройства: ')
        inpt_manufacturer = input('Введите производителя: ')
        if result == 'Принтер' or result == 'принтер':
            printer = Printer(inpt_color, inpt_barcode, inpt_manufacturer,
                              inpt_country, inpt_amount)
            print(printer.__str__())
            print(printer.to_print(200))
        elif result == 'Сканер' or result == 'сканер':
            scaner = Scan(inpt_color, inpt_barcode, inpt_manufacturer,
                              inpt_country, inpt_amount)
            print(scaner.__str__())
            print(scaner.to_scan(300))
        elif result == 'Ксерокс' or result == 'ксерокс':
            xerox = Xerox(inpt_color, inpt_barcode, inpt_manufacturer,
                          inpt_country, inpt_amount)
            print(xerox.__str__())
            print(xerox.to_xerox(300))
        break
while True:
    report(input('Введите название устройства, о котором хотите сделать отчёт: '))



