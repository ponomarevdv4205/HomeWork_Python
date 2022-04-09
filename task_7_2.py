'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке (0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

# Решение:

import random

n = int(input('Введите сколько будет случайных чисел в создаваемом массиве (массив будет заполняться случайными вещественными числами от 0 до 50): '))
mas1 = [0] * n
for i in range(n):
    mas1[i-1] = float(random.random() * 50)

print(f'Исходный массив: {mas1}')

# Сортировка методом слияния по возрастанию:

def my_sort(mas):

    if len(mas) < 2:
        return mas

    left_part = my_sort(mas[:len(mas) // 2])
    right_part = my_sort(mas[len(mas) // 2:len(mas)])

    i = 0
    j = 0
    n = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            mas[n] = left_part[i]
            i = i + 1
        else:
            mas[n] = right_part[j]
            j = j + 1
        n = n + 1

    while i < len(left_part):
        mas[n] = left_part[i]
        i = i + 1
        n = n + 1

    while j < len(right_part):
        mas[n] = right_part[j]
        j = j + 1
        n = n + 1

    return mas


print(f'Отсортированный массив по возрастанию методом слияния: {my_sort(mas1)}')
