'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

# Решение:

import random

while True:
    n = int(input('Введите сколько будет случайных чисел в создаваемом массиве (массив будет заполняться случайными числами от 0 до 10): '))
    if n > 0:
        mas1 = [0] * n
        for i in range(n):
            mas1[i-1] = int(random.random() * 10)
        break

print(f'Исходный массив: {mas1}')

min_item = 0
min_idx = 0
max_item = 0
max_idx = 0

min_item = mas1[0]
min_idx = 0
max_item = mas1[0]
max_idx = 0

for idx, item in enumerate(mas1):
    if item <= min_item and item != min_item:
        min_item = item
        min_idx = idx
    elif item > max_item or item == max_item:
        max_item = item
        max_idx = idx

print(f'Минимальный элемент равен {min_item}, а его индекс (первый раз встречающийся) равен {min_idx}')
print(f'Максимальный элемент равен {max_item}, а его индекс (последний раз встречающийся) равен {max_idx}')

rezult = 0

if min_idx < max_idx:
    for i in mas1[min_idx + 1:max_idx]:
        rezult = i + rezult
elif min_idx > max_idx:
    for i in mas1[max_idx + 1:min_idx]:
        rezult = i +rezult

print(f'Сумма значений элементов между ними равна {rezult}')
