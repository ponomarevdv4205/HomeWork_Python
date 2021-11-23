'''
Задание:
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
'''


# Решение:

class Warehouse:
    def __init__(self, company_name='Моя компания'):
        self.company_name = company_name


class Office_Equipment(Warehouse):
    def __init__(self, id, manufacturer, year_release, color):
        super().__init__()
        self.id = id
        self.manufacturer = manufacturer
        self.year_release = year_release
        self.color = color


class Printer(Office_Equipment):
    def __init__(self, id, manufacturer, year_release, color, printer_type):
        super().__init__(id, manufacturer, year_release, color)
        self.printer_type = printer_type


class Scanner(Office_Equipment):
    def __init__(self, id, manufacturer, year_release, color, scanner_type):
        super().__init__(id, manufacturer, year_release, color)
        self.scanner_type = scanner_type


class Xerox(Office_Equipment):
    def __init__(self, id, manufacturer, year_release, color, xerox_type):
        super().__init__(id, manufacturer, year_release, color)
        self.xerox_type = xerox_type