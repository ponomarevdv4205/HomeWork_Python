'''
Задание:
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''

#Решение:
import ast

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = ast.literal_eval(is_police)

    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 60:
            return f'Текущая скорость автомобиля: {self.speed} - скорость превышена!!!'
        return f'Текущая скорость автомобиля: {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            return f'Текущая скорость автомобиля: {self.speed} - скорость превышена!!!'
        return f'Текущая скорость автомобиля: {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

user_input = input("Введите через запятую скорость, цвет, имя, полиция (True или False), например: 80,красная,Моя машина,False: ").split(',')
user_input_direction = input("Куда повернула машина? (например: направо) ")
result_Car = Car(user_input[0], user_input[1], user_input[2], user_input[3])
result_TownCar = TownCar(user_input[0], user_input[1], user_input[2], user_input[3])
result_SportCar = SportCar(user_input[0], user_input[1], user_input[2], user_input[3])
result_WorkCarr = WorkCar(user_input[0], user_input[1], user_input[2], user_input[3])
result_PoliceCar = PoliceCar(user_input[0], user_input[1], user_input[2], user_input[3])

print("Проверка атрибутов и методов классов:")
print(f'Атрибут "speed" = {result_Car.speed}')
print(f'Атрибут "color" = {result_Car.color}')
print(f'Атрибут "name" = {result_Car.name}')
print(f'Атрибут "is_police" = {result_Car.is_police} и это {type(result_Car.is_police)}')
print(f'Для базового класса Car метод go выводит следующий результат: {result_Car.go()}')
print(f'Для базового класса Car метод stop выводит следующий результат: {result_Car.stop()}')
print(f'Для базового класса Car метод turn выводит следующий результат: {result_Car.turn(user_input_direction)}')
print(f'Для базового класса Car метод show_speed выводит следующий результат: {result_Car.show_speed()}')
print(f'Для класса TownCar метод show_speed выводит следующий результат: {result_TownCar.show_speed()}')
print(f'Для класса SportCar метод show_speed выводит следующий результат: {result_SportCar.show_speed()}')
print(f'Для класса WorkCarr метод show_speed выводит следующий результат: {result_WorkCarr.show_speed()}')
print(f'Для класса PoliceCar метод show_speed выводит следующий результат: {result_PoliceCar.show_speed()}')