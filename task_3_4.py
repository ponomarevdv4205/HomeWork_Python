'''
4. Определить, какое число в массиве встречается чаще всего.
'''

# Решение:

import random

n = int(input('Введите сколько будет случайных чисел в создаваемом массиве (массив будет заполняться случайными числами от 0 до 10): '))
mas1 = [0] * n
for i in range(n):
    mas1[i-1] = int(random.random() * 10)


print(f'Исходный массив: {mas1}')

item_count = 0
rezult = []

for i in mas1:
    if mas1.count(i) > item_count:
        item_count = mas1.count(i)
for i in mas1:
    if mas1.count(i) == item_count:
        rezult.append(i)

print(f'Числа {list(set(rezult))} встречаются чаще всего, а именно {item_count} раз.')