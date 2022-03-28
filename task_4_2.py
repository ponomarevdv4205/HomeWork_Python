'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
'''

# Решение:

import math, cProfile

num = int(input('Введите i-е по счёту простое число (для тестирования подойдёт, например, число 1000): '))

# 1) Алгоритм нахождения простого числа без использования «Решета Эратосфена»:

def metod_1(item):
    rezult = [2]
    num = 3
    while len(rezult) < item:
        flag = True
        for j in rezult.copy():
            if num % j == 0:
                flag = False
                break
        if flag:
            rezult.append(num)
        num += 1
    return rezult[-1]


# 2) Алгоритм нахождения простого числа с использованием «Решета Эратосфена»:

def metod_2(item):
    max_item = function_1(item)
    rezult = [i for i in range(2, max_item)]

    for num in rezult:
        if rezult.index(num) <= num - 1:
            for j in range(2, len(rezult)):
                if num * j in rezult[num:]:
                    rezult.remove(num * j)
        else:
            break
    return rezult[item - 1]


def function_1(item):
    num_1 = 0
    num_2 = 2
    while num_1 <= item:
        num_1 = num_2 / math.log(num_2)
        num_2 += 1
    return num_2


print('Алгоритм № 1 без использования «Решета Эратосфена»:', f'Это число: {metod_1(num)}')
print('Алгоритм № 2 с использованием «Решета Эратосфена»:', f'Это число: {metod_2(num)}')

print()
print('Анализ количества вызовов и времени исполнения по Алгоритму № 1:')
cProfile.run('metod_1(num)')

print('Анализ количества вызовов и времени исполнения по Алгоритму № 2:')
cProfile.run('metod_2(num)')

# ВЫВОДЫ:
''' При тестировании на моём ПК двух алгоритмов на числе по порядку 1000 следующие результаты:
Алгоритм № 1 (без «Решета Эратосфена»): 16838 вызовов функций за 0,029 секунды
Алгоритм № 2 (с «Решетом Эратосфена»): 19372 вызовов функций за 2,564 секунды
Алгоритм № 2 более эффективен по времени выполнения.
'''