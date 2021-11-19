'''
Задание:
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__floordiv__, __truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
'''

#Решение:

class Cell:
    def __init__(self, kol_cells):
        self.__kol_cells = kol_cells

    def __add__(self, other):
        return self.__kol_cells + other.__kol_cells

    def __sub__(self, other):
        if self.__kol_cells > other.__kol_cells: return self.__kol_cells - other.__kol_cells
        else: return f'Количество ячеек первой клетки меньше количества ячеек второй клетки, поэтому вычитание не допустимо!'

    def __mul__(self, other):
        return self.__kol_cells * other.__kol_cells

    def __floordiv__(self, other):
        return self.__kol_cells // other.__kol_cells

    def __truediv__(self, other):
        return self.__kol_cells // other.__kol_cells

    def make_order(self, n):
        rezult = ''
        row = self.__kol_cells // n
        for i in range(row):
            rezult += '*'*n + r'\n'
        if self.__kol_cells % n == 0: rezult = rezult[:-2]
        rezult += '*'*(self.__kol_cells - (row*n))
        return rezult


cell_1 = Cell(int(input('Введите количество ячеек первой клетки: ')))
cell_2 = Cell(int(input('Введите количество ячеек второй клетки: ')))
row = int(input('Введите количество ячеек в ряду: '))
print(f'Результат сложения двух клеток: {cell_1 + cell_2}')
print(f'Результат вычитания двух клеток: {cell_1 - cell_2}')
print(f'Результат умножения двух клеток: {cell_1 * cell_2}')
print(f'Результат деления (по условиям задачи - целочисленное деление) двух клеток (оператором /): {cell_1 / cell_2}')
print(f'Результат деления (по условиям задачи - целочисленное деление) двух клеток (оператором //): {cell_1 // cell_2}')
print(f'Организация первой ячейки по рядам выглядит следующим образом: {cell_1.make_order(row)}')
print(f'Организация второй ячейки по рядам выглядит следующим образом: {cell_2.make_order(row)}')