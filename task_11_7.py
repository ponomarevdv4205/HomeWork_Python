'''
Задание:
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


# Решение:

class Complex_Number:
    def __init__(self, natural, imaginary):
        self.natural = natural
        self.imaginary = imaginary

    def __add__(self, other):
        a = self.natural + other.natural
        b = self.imaginary + other.imaginary
        return f'{a} + {b}i'

    def __mul__(self, other):
        a = self.natural * other.natural
        ai = self.natural * other.imaginary
        bi = self.imaginary * other.natural
        bii = self.imaginary * other.imaginary
        a = a - bii
        b = ai + bi
        return f'{a} + {b}i'


user_input_1 = input("Введите через пробел натуральную и мнимую часть ПЕРВОГО комплексного числа: ").split()
user_input_2 = input("Введите через пробел натуральную и мнимую часть ВТОРОГО комплексного числа: ").split()

complex_number_1 = Complex_Number(int(user_input_1[0]), int(user_input_1[1]))
complex_number_2 = Complex_Number(int(user_input_2[0]), int(user_input_2[1]))

print("Результат сложения двух комплексных чисел равен: {}".format(complex_number_1 + complex_number_2))
print("Результат умножения двух комплексных чисел равен: {}".format(complex_number_1 * complex_number_2))