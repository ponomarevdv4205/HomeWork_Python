'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

# Решение:

from random import random

mas1 = [0]*5
for i in range(5):
    mas2 = [0] * 5
    for j in range(5):
        mas2[j] = int(random() * 10)
        mas1[i] = mas2

print(f'Создадим исходную матрицу размером 5х5: {mas1}')

print("Исходный массив в виде матрицы:")
for i in range(5):
    print(*mas1[i], end="\n")

mas_rezult = []
for i in range(5):
    mas_rezult_ = []
    for j in range(5):
        mas_rezult_.append(mas1[j][i])
    mas_rezult.append(mas_rezult_)

mas_rezult2 = []
for i in mas_rezult:
    min_item = i[0]
    for j in i:
        if j < min_item:
            min_item = j
    mas_rezult2.append(min_item)

print(f'Минимальное значение каждого столбца: {mas_rezult2}')

max_item = int(mas_rezult2[0])
for i in mas_rezult2:
    if int(i) > max_item:
        max_item = i

print(f'Максимальный элемент среди минимальных элементов столбцов равен: {max_item}')