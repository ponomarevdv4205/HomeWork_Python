'''
Задание:
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
'''

#Решение:

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.len_column = len(self.matrix)
        self.len_line = len(self.matrix[0])

    def __str__(self):
        result = ''
        for i in self.matrix:
            result = result + '| '
            for j in i:
                result = result + f'{j} '
            result = result + '|\n'
        return result

    def matrix_addition(self, other):
        max_len_column = max(len(self.matrix), len(other.matrix))
        len_column_self = max_len_column - len(self.matrix)
        len_column_other = max_len_column - len(other.matrix)
        if len_column_self > 0:
            for i in range(len_column_self):
                result = []
                for j in range(self.len_line):
                    result.append(0)
                self.matrix.append(result)

        if len_column_other > 0:
            for i in range(len_column_other):
                result = []
                for j in range(other.len_line):
                    result.append(0)
                other.matrix.append(result)

        result =[]
        for i in range(max_len_column):
            max_len_line = max(len(self.matrix[i]), len(other.matrix[i]))
            result_line = []
            for j in range(max_len_line):
                if j > self.len_line-1: a = 0
                else: a = self.matrix[i][j]
                if j > other.len_line-1: b = 0
                else: b = other.matrix[i][j]
                result_line.append(a+b)
            result.append(result_line)
        return result

    def __add__(self, other):
        if self.len_column != other.len_column or self.len_line != other.len_line:
            print('Так как матрицы разного размера, то операция сложения невозможна!')
            print('Но если мы дополним одну матрицу значениями 0 до размера другой матрицы, то их можно будет сложить и результат будет следующий:')
            return Matrix.matrix_addition(self, other)
        else:
            return Matrix.matrix_addition(self, other)


matrix_1 = Matrix([
    [31, 22],
    [37, 43],
    [51, 86]
])

matrix_2 = Matrix([
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8]
])

matrix_3 = Matrix([
    [3, 5, 8, 3],
    [8, 3, 7, 1]
])

matrix_4 = Matrix([
    [3, 5],
    [2, 4],
    [-1, 64]
])

print("Печать матриц в привычном виде:")
print(f'Матрица 1:\n{matrix_1}')
print(f'Матрица 2:\n{matrix_2}')
print(f'Матрица 3:\n{matrix_3}')
print(f'Матрица 4:\n{matrix_4}')

print('Результат сложения Матрицы 1 и Матрицы 2 равен:')
print(Matrix(matrix_1 + matrix_2))
print('Результат сложения Матрицы 1 и Матрицы 3 равен:')
print(Matrix(matrix_1 + matrix_3))
print('Результат сложения Матрицы 2 и Матрицы 3 равен:')
print(Matrix(matrix_2 + matrix_3))
print('Результат сложения Матрицы 1 и Матрицы 4 равен:')
print(Matrix(matrix_1 + matrix_4))