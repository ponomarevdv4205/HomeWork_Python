'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
'''

# Решение:

# На моем ПК установлена 64-разрядная операционная система, Python 3.9

# Ниже три метода перебора числа в обратную сторону:

import sys, math

num = '5648988464112306515905956565651569979565216520651605652362362377122131647657215125661346313765651065656979767331646799463'

def metod_1(num):
    rezult =''
    for item in range(len(num) - 1, -1, -1):
        yield rezult + num[item]


def metod_2(num):
    rezult = ''
    for idx, item in enumerate(num):
        yield item + rezult


def recursion(n):
    if len(n) < 1:
        return n
    return n[-1] + recursion(n[:-1])


# Оцениваем выделенный объем памяти под эти объекты:

print('Справочно: Число байт под объект (переменную) num:', sys.getsizeof(num), ', а ссылок на объект:', sys.getrefcount(num))
print('Число байт под объект (метод) через range:', sys.getsizeof(metod_1(num)), ', а ссылок на объект:', sys.getrefcount(metod_1(num)))
print('Число байт под объект (метод) через enumerate:',sys.getsizeof(metod_2(num)), ', а ссылок на объект:', sys.getrefcount(metod_2(num)))
print('Число байт под объект (метод) через recursion:',sys.getsizeof(recursion(num)), ', а ссылок на объект:', sys.getrefcount(recursion(num)))
# ВЫВОД: видим, что под рекурсию занимается больше памяти

# Ниже представлены алгоритмы нахождения простого числа:

num1 = 1000
# 1) Алгоритм нахождения простого числа без использования «Решета Эратосфена»:

def metod_3(item):
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

def metod_4(item):
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

# Оцениваем выделенный объем памяти под эти объекты:

print('-'*200)
print('Справочно: Число байт под объект (переменную) num1:', sys.getsizeof(num1), ', а ссылок на объект:', sys.getrefcount(num1))
print('Число байт под объект (метод) без использования «Решета Эратосфена»:', sys.getsizeof(metod_3(num1)), ', а ссылок на объект:', sys.getrefcount(metod_3(num1)))
print('Число байт под объект (метод) с использованием «Решета Эратосфена»:', sys.getsizeof(metod_4(num1)), ', а ссылок на объект:', sys.getrefcount(metod_4(num1)))
print('Число байт под объект (ункцию) function_1:', sys.getsizeof(function_1(num1)), ', а ссылок на объект:', sys.getrefcount(function_1(num1)))
# ВЫВОД: видим, под данные объекты занимается равный объем памяти

# Ниже для анализа создадим массив из одних и тех же значений в виде списка и в виде кортежа:

mas_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mas_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Оцениваем выделенный объем памяти под эти объекты:
print('-'*200)
print('Число байт под объект mas_1 (список):', sys.getsizeof(mas_1), ', а ссылок на объект:', sys.getrefcount(mas_1))
print('Число байт под объект mas_2 (кортеж):', sys.getsizeof(mas_2), ', а ссылок на объект:', sys.getrefcount(mas_2))
# ВЫВОД: видим, что размер списка больше, чем кортежа (152 и 120 байт соответственно). Размер не зависит от разрядности чисел, а зависит от размера массива.
