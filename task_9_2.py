'''
Задание:
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''

#Решение:
class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def __mul__(self, other):
        return self._length * self._width * other.mass * other.thickness

class Thickness:
    mass = 25
    thickness = 0.005

my_list = input('Введите значение длинны и ширины полотна дороги (в метрах через запятую): ').split(',')
print(f'Масса асфальта равна: {my_list[0]} м * {my_list[1]} м * {Thickness.mass} кг * {int(Thickness.thickness*1000)} см = {int(Road(my_list[0], my_list[1])*Thickness())} т')