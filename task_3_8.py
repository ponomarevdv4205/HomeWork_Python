'''
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''

# Решение:

from random import random

mas1 = [0]*5
for i in range(5):
    mas2 = [0] * 4
    for j in range(4):
        mas2[j] = int(random() * 10)
        mas1[i] = mas2

print(f'Исходный массив в виде списка: {mas1}')

print("Исходный массив в виде матрицы (в конце сумма каждой строки):")
for i in range(5):
    sum = 0
    for j in mas1[i]:
        sum += j
    print(*mas1[i], '|', sum, end="\n")

