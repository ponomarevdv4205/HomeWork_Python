'''
Задание:
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

#Решение:

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {10000:1000, 20000:2000, 30000:3000, 40000:4000, 50000:5000, 60000:6000, 70000:7000, 80000:8000, 90000:9000, 100000:10000}

class Position(Worker):
    def __init__(self, name, surname, position, wage):
        super().__init__(name, surname, position)
        self.wage = int(wage)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        for idx, val in self._income.items():
            if self.wage == idx:
                return idx + val

user_input = input('Введите через запятую имя, фамилию, должность и оклад работника (например: Иван,Дудкин,начальник,100000): ').split(',')
result = Position(user_input[0],user_input[1],user_input[2],user_input[3])
print('Проверка значений атрибутов:')
print(f'Атрибут "name" = {result.name}')
print(f'Атрибут "surname" = {result.surname}')
print(f'Атрибут "position" = {result.position}')
print(f'Атрибут "income" = {result._income}')
print(f'Полное имя сотрудника: {result.get_full_name()}')
print(f'Доход сотрудника: {result.get_total_income()}')