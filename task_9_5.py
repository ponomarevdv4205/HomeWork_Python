'''
Задание:
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

#Решение:
class Stationery:
    def __init__(self, title = '(базовый класс)'):
        self.title = title

    @property
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = '(класс Pen)'

    @property
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = '(класс Pencil)'

    @property
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = '(класс Handle)'

    @property
    def draw(self):
        return f'Запуск отрисовки {self.title}'


print(f'Метод draw для базового класса выдаёт результат: {Stationery().draw}')
print(f'Метод draw для класса Pen выдаёт результат: {Pen().draw}')
print(f'Метод draw для класса Pencil выдаёт результат: {Pencil().draw}')
print(f'Метод draw для класса Handle выдаёт результат: {Handle().draw}')