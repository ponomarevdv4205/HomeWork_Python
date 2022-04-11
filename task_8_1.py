'''
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''

# Решение:

import collections
import random
import string as st
import hashlib

var = 2
while var != 0 and var != 1:
    var = int(input("Введите способ формирования исходной строки (0 - случайным образом, 1 - ввод с клавиатуры): "))

if var == 0:
    N = int(input("Введите длину N строки, в которой мы будем искать и подсчитывать количество различных подстрок (строка будет формироваться из случайных маленьких латинских букв): "))
    my_str = ''
    for i in range(N):
        my_str = my_str + st.ascii_lowercase[random.randint(97, 122) - 97]
else:
    my_str = input("Введите строку, в которой будем искать и подсчитывать количество различных подстрок: ")

print(f'Исходная заданная строка: {my_str}')

# Функция записи различных подстрок в список и определение их количества:
def my_counter(s):
    my_list = []
    len_sub = len(s)
    for i in range(len_sub):
        for j in range(len_sub+1):
            if s[i:j] != '' and s[i:j] != s:
                my_list.append(s[i:j])
    counter = collections.Counter()
    for word in my_list:
        counter[word] += 1
    return counter


# Функция поиска подстраки по хеш-значению:
def my_hash(s, t):
    my_list = []
    len_sub = len(s)
    for i in range(len_sub):
        for j in range(len_sub+1):
            if s[i:j] != '' and s[i:j] != s:
                my_list.append(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    counter = collections.Counter()
    for word in my_list:
        counter[word] += 1
    t_hash = hashlib.sha1(t.encode('utf-8')).hexdigest()
    return counter.setdefault(t_hash, 0)


print("Ниже представлены всевозможные варианты подстрок и их количество из исходной строки:")
d1 = my_counter(my_str)
for i in d1.items():
    print(*i)

print(f'Еще раз: Исходная заданная строка: {my_str}')
t = ''
while t != '0':
    t = input(f'Введите искомую подстраку из заданного слова \"{my_str}\" (0 - выход из программы): ')
    if t == '0':
        print('Программа завершена!')
        break
    else:
        print(f'Данная подстрака встречается в исходной строке {my_hash(my_str, t)} раз')
