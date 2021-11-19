'''
Задание:
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
'''


# Решение:

class Сlothes():
    def __init__(self, V, H):
        self.V = int(V)
        self.H = int(H)

    @property
    def fabric_consumption(self):
        return f'Этой строкой напечатался базовый метод для определения расхода ткани'

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption

class Coat(Сlothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    @property
    def fabric_consumption(self):
        return (self.V / 6.5 + 0.5)

class Suit(Сlothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    @property
    def fabric_consumption(self):
        return (2 * self.H + 0.3)

a = input('Введите через запятую параметры одежды (размер и рост): ').split(',')
print(Сlothes(a[0], a[1]).fabric_consumption)
print(f'Расход ткани для пальто = {Coat(a[0], a[1]).fabric_consumption}')
print(f'Расход ткани для костюма = {Suit(a[0], a[1]).fabric_consumption}')
print(f'Общий расход ткани = {Coat(a[0], a[1]) + Suit(a[0], a[1])}')
