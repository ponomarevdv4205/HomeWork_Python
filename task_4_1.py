'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

# Решение:

import timeit

num = '5648988464112306515905956565651569979565216520651605652362362377122131647657215125661346313765651065656979767331646799463'

print(f'Проверим скорость работы трех вариантов перебора числа в обратную сторону. Число {num}')

def metod_1(num):
    rezult =''
    for item in range(len(num) - 1, -1, -1):
        yield rezult + num[item]

print('Число в обратную сторону (метод через range): ', *list(metod_1(num)))

def metod_2(num):
    rezult = ''
    for idx, item in enumerate(num):
        yield item + rezult

print('Число в обратную сторону (метод через enumerate): ', *list(metod_2(num)))

def recursion(n):
    if len(n) < 1:
        return n
    return n[-1] + recursion(n[:-1])

print('Число в обратную сторону (метод через рекурсию): ', *list(recursion(num)))

# Оцениваем время выполнения различных алгоритмов:

s1 = """\
def metod_1(num):
    rezult =''
    for item in range(len(num) - 1, -1, -1):
        yield rezult + num[item]
"""

s2 = """\
def metod_2(num):
    rezult = ''
    for idx, item in enumerate(num):
        yield item + rezult
"""

s3 = """\
def recursion(n):
    if len(n) < 1:
        return n
    return n[-1] + recursion(n[:-1])
"""

print('Время работы метода через range (в повторении 100000000 раз): ', timeit.timeit(stmt=s1, number=100000000))
print('Время работы метода через enumerate (в повторении 100000000 раз): ', timeit.timeit(stmt=s2, number=100000000))
print('Время работы метода через рекурсию (в повторении 100000000 раз): ', timeit.timeit(stmt=s3, number=100000000))

# ВЫВОД:
# Видим, что метод через рекурсию хоть и выглядит по коду проще, но на моём ПК его обработка в тестируемых условиях занимает на 1,5 секунды больше.