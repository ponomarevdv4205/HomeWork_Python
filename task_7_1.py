'''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

# Решение:

import random

n = int(input('Введите сколько будет случайных чисел в создаваемом массиве (массив будет заполняться случайными числами от -100 до 100): '))
mas1 = [0] * n
for i in range(n):
    mas1[i-1] = int(random.random() * 200) - 100

print(f'Исходный массив: {mas1}')

# Сортировка методом "пузырька"  по убыванию:

def my_sort(mas):
    n = 1
    m = len(mas)
    while n < m:
        flag = True
        for i in range(m - n, 0, -1):
            if mas[i] > mas[i - 1]:
                mas[i], mas[i - 1] = mas[i - 1], mas[i]
                flag = False
        if flag == True:
            n += 1
    return mas


print(f'Отсортированный массив по убыванию: {my_sort(mas1)}')
