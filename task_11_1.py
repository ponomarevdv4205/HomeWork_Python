'''
Задание:
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

#Решение:

class Data:
    def __init__(self, data):
        self.data = data.split('-')

    def __str__(self):
        return self.data

    @classmethod
    def my_classmethod(cls, data):
        result = []
        for i in cls(data).__str__():
            result.append(int(i))
        return result

    @staticmethod
    def my_staticmethod(user_input):
        result = ''
        data_user = Data.my_classmethod(user_input)
        if not 0 < data_user[0] <=31:
            result += "Вы ввели число не в диапазоне от 0 до 31.\n"
        if not 0 < data_user[1] <=12:
            result += "Вы ввели месяц не в диапазоне от 0 до 12.\n"
        if not 1900 < data_user[2] <=2021:
            result += "Вы ввели год не в диапазоне от 1900 до 2021.\n"
        if result != '':
            result += 'Скрипт остановлен.'
            return result
        return data_user

user_input = input("Введите дату в виде строки формата «день-месяц-год»: ")
print(f'Результат работы метода с декоратором @classmethod:\n{Data.my_classmethod(user_input)}')
print(f'Результат работы метода с декоратором @staticmethod:\n{Data.my_staticmethod(user_input)}')