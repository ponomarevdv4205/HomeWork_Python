'''
Задание:
5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
'''


# Решение:

class Warehouse:
    my_dict_printer_in = {}
    my_dict_scanner_in = {}
    my_dict_xerox_in = {}
    my_dict_printer_out = {}
    my_dict_scanner_out = {}
    my_dict_xerox_out = {}

    def __init__(self, company_name='Моя компания'):
        self.company_name = company_name

    @property
    def __str__(self):
        return f'"{self.company_name}"'


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

    def printer_in(self):
        Warehouse.my_dict_printer_in.setdefault(self.id,
                                                [self.manufacturer, self.year_release, self.color, self.printer_type])
        print(f'Принтер с id {self.id} оприходован на склад!')

    def printer_out(self):
        Warehouse.my_dict_printer_out.setdefault(self.id,
                                                 [self.manufacturer, self.year_release, self.color, self.printer_type])
        print(f'Принтер с id {self.id} списан со склада!')

    def __str__(parameter):
        if parameter == 1:
            return Warehouse.my_dict_printer_in
        if parameter == 2:
            return Warehouse.my_dict_printer_out


class Scanner(Office_Equipment):
    def __init__(self, id, manufacturer, year_release, color, scanner_type):
        super().__init__(id, manufacturer, year_release, color)
        self.scanner_type = scanner_type

    def scanner_in(self):
        Warehouse.my_dict_scanner_in.setdefault(self.id,
                                                [self.manufacturer, self.year_release, self.color, self.scanner_type])
        print(f'Сканер с id {self.id} оприходован на склад!')

    def scanner_out(self):
        Warehouse.my_dict_scanner_out.setdefault(self.id,
                                                 [self.manufacturer, self.year_release, self.color, self.scanner_type])
        print(f'Сканер с id {self.id} списан со склада!')

    def __str__(parameter):
        if parameter == 1:
            return Warehouse.my_dict_scanner_in
        if parameter == 2:
            return Warehouse.my_dict_scanner_out


class Xerox(Office_Equipment):
    def __init__(self, id, manufacturer, year_release, color, xerox_type):
        super().__init__(id, manufacturer, year_release, color)
        self.xerox_type = xerox_type

    def xerox_in(self):
        Warehouse.my_dict_xerox_in.setdefault(self.id,
                                              [self.manufacturer, self.year_release, self.color, self.xerox_type])
        print(f'Ксерокс с id {self.id} оприходован на склад!')

    def xerox_out(self):
        Warehouse.my_dict_xerox_out.setdefault(self.id,
                                               [self.manufacturer, self.year_release, self.color, self.xerox_type])
        print(f'Ксерокс с id {self.id} списан со склада!')

    def __str__(parameter):
        if parameter == 1:
            return Warehouse.my_dict_xerox_in
        if parameter == 2:
            return Warehouse.my_dict_xerox_out


while True:
    action = input(
        'Выберите действие, которое будите выполнять (1 - приём на склад; 2 - передачу со склада; любой другой ввод - выход из ввода): ')

    if action == '1':
        action_type = input(
            'Выберите тип оргтехники, который будите принимать на склад (1 - принтер; 2 - сканер; 3 - ксерокс; любой другой ввод - выход из ввода): ')
        if action_type == '1':
            user_input = input(
                'Введите через запятую параметры передаваемого на склад принтера (id,производитель,год выпуска,цвет,тип принтера): ').split(
                ',')
            Printer(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).printer_in()
        elif action_type == '2':
            user_input = input(
                'Введите через запятую параметры передаваемого на склад сканера (id,производитель,год выпуска,цвет,тип сканера): ').split(
                ',')
            Scanner(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).scanner_in()
        elif action_type == '3':
            user_input = input(
                'Введите через запятую параметры передаваемого на склад ксерокса (id,производитель,год выпуска,цвет,тип ксерокса): ').split(
                ',')
            Xerox(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).xerox_in()
        else:
            break
    elif action == '2':
        action_type = input(
            'Выберите тип оргтехники, который будите передовать со склада (1 - принтер; 2 - сканер; 3 - ксерокс; любой другой ввод - выход из ввода): ')
        if action_type == '1':
            user_input = input(
                'Введите через запятую параметры передаваемого со склада принтера (id,производитель,год выпуска,цвет,тип принтера): ').split(
                ',')
            Printer(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).printer_out()
        elif action_type == '2':
            user_input = input(
                'Введите через запятую параметры передаваемого со склада сканера (id,производитель,год выпуска,цвет,тип сканера): ').split(
                ',')
            Scanner(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).scanner_out()
        elif action_type == '3':
            user_input = input(
                'Введите через запятую параметры передаваемого со склада ксерокса (id,производитель,год выпуска,цвет,тип ксерокса): ').split(
                ',')
            Xerox(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).xerox_out()
        else:
            break
    else:
        break

print('\n' + '*' * 70 + f' Движения по складу компании {Warehouse().__str__} ' + '*' * 70)
print(f'Список поступивших на склад принтеров:\n{Printer.__str__(1)}')
print(f'Список переданных со склада принтеров:\n{Printer.__str__(2)}')
print(f'Список поступивших на склад сканеров:\n{Scanner.__str__(1)}')
print(f'Список переданных со склада сканеров:\n{Scanner.__str__(2)}')
print(f'Список поступивших на склад ксероксов:\n{Xerox.__str__(1)}')
print(f'Список переданных со склада ксероксов:\n{Xerox.__str__(2)}')