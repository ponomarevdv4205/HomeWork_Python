'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

# Решение:

import random

n = int(input('Введите сколько будет случайных чисел: '))
mas1 = [0] * n
m = int(input('Введите до какого числа (начиная с 0) генерировать случайные числа: '))
for i in range(n):
    mas1[i-1] = int(random.random() * m)

print(f'Исходный массив случайных чисел: {mas1}')

min_item = mas1[0]
min_idx = 0
max_item = mas1[0]
max_idx = 0

for idx, item in enumerate(mas1):
    if item <= min_item:
        min_item = item
        min_idx = idx
    elif item > max_item:
        max_item = item
        max_idx = idx

mas1[min_idx] = max_item
mas1[max_idx] = min_item

print(f'Поменяли местами минимальный ({min_item}) и максимальный ({max_item}) элементы: {mas1}')