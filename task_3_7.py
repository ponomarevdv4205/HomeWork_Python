'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

# Решение:

import random

kol = 2 # Сколько оставлять наименьших элементов (при необходимости может задавать пользователь)

while True:
    n = int(input('Введите сколько будет случайных чисел в создаваемом массиве (массив будет заполняться случайными числами от 0 до 10): '))
    if n > kol:
        mas1 = [0] * n
        for i in range(n):
            mas1[i-1] = int(random.random() * 10)
        break

print(f'Исходный массив: {mas1}')

def min_mas(mas, kol):
    min_item1 = mas[0]
    min_idx1 = 0
    if kol <= 1:
        for idx, item in enumerate(mas1):
            if item <= min_item1:
                min_item1 = item
                min_idx1 = idx
        del mas[min_idx1]
        return min_item1
    kol -= 1
    return str(min_mas(mas, kol)) + ", " + str(min_mas(mas, kol-1))

print(f'Два наименьших элемента: {min_mas(mas1, kol)}')