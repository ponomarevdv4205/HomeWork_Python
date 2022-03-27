'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

# Решение:

import random

n = int(input('Введите сколько будет случайных чисел в создаваемом массиве (массив будет заполняться случайными числами от -10 до 10): '))
mas1 = [0] * n
for i in range(n):
    mas1[i-1] = int(random.random() * 20) - 10

print(f'Исходный массив: {mas1}')

item_idx = 0
rezult = 0
flag_0 = False

for i in range(n):
    if mas1[i] < rezult:
        rezult = mas1[i]
        item_idx = i
        flag_0 = True

if flag_0 == True:
    print(f'Максимальный отрицательный элемент это {rezult}, его индекс {item_idx}, а порядковый номер в массиве {item_idx + 1}')
else:
    print("Отрицательных значений в массиве нет!")
