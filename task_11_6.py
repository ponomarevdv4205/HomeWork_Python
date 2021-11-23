'''
Задание:
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
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

    @staticmethod
    def id_error(id):
        try:
            if id.isdigit():
                return True
            else:
                raise My_Error_ID()
        except My_Error_ID:
            return False

    @staticmethod
    def str_error(my_str):
        try:
            if len(my_str) == 5:
                return True
            elif len(my_str) < 5:
                raise My_Error_STR("*** ВНИМАНИЕ!!! Вы ввели не все параметры оборудования! ***")
                return False
            else:
                raise My_Error_STR("*** ВНИМАНИЕ!!! Вы ввели больше параметров, чем нужно! ***")
                return False
        except My_Error_STR:
            return False


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


class My_Error_ID(Exception):
    def __init__(self, txt="*** ВНИМАНИЕ!!! id номер должен быть только целым числом! ***"):
        print(txt)


class My_Error_STR(Exception):
    def __init__(self, txt="*** ВНИМАНИЕ!!! Не корректный ввод параметров! ***"):
        print(txt)


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
            err_str = Office_Equipment.str_error(user_input)
            err_id = Office_Equipment.id_error(user_input[0])
            if err_id == False or err_str == False:
                continue
            Printer(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).printer_in()
        elif action_type == '2':
            user_input = input(
                'Введите через запятую параметры передаваемого на склад сканера (id,производитель,год выпуска,цвет,тип сканера): ').split(
                ',')
            err_str = Office_Equipment.str_error(user_input)
            err_id = Office_Equipment.id_error(user_input[0])
            if err_id == False or err_str == False:
                continue
            Scanner(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).scanner_in()
        elif action_type == '3':
            user_input = input(
                'Введите через запятую параметры передаваемого на склад ксерокса (id,производитель,год выпуска,цвет,тип ксерокса): ').split(
                ',')
            err_str = Office_Equipment.str_error(user_input)
            err_id = Office_Equipment.id_error(user_input[0])
            if err_id == False or err_str == False:
                continue
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
            err_str = Office_Equipment.str_error(user_input)
            err_id = Office_Equipment.id_error(user_input[0])
            if err_id == False or err_str == False:
                continue
            Printer(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).printer_out()
        elif action_type == '2':
            user_input = input(
                'Введите через запятую параметры передаваемого со склада сканера (id,производитель,год выпуска,цвет,тип сканера): ').split(
                ',')
            err_str = Office_Equipment.str_error(user_input)
            err_id = Office_Equipment.id_error(user_input[0])
            if err_id == False or err_str == False:
                continue
            Scanner(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]).scanner_out()
        elif action_type == '3':
            user_input = input(
                'Введите через запятую параметры передаваемого со склада ксерокса (id,производитель,год выпуска,цвет,тип ксерокса): ').split(
                ',')
            err_str = Office_Equipment.str_error(user_input)
            err_id = Office_Equipment.id_error(user_input[0])
            if err_id == False or err_str == False:
                continue
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