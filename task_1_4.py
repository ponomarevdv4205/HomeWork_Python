'''
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

# Решение:

# Используем модуль времени, т.к. секунды/наносекунды каждого события будут разными
import time
import string as st

x1, x2 = map(int, input('Введите через пробел диапазон генерации случайного целого числа (x1, x2): ').split())

# Проверка на максимальное число (выстраиваем правильно диапазон чисел):
max_x = x2
if x1 > x2:
    x2 = x1
    x1 = max_x

now_sec = str(time.time())
rnd = int(now_sec[::-1][:3:])/1000
result = x1 + rnd*(x2 - x1)

if int(str(result*1000//1)[:-2][1:]) >= 500:
    result = str(1 + result*1000//1000)[:-2]
else:
    result = str(result * 1000 // 1000)[:-2]

print(f'Случайное целое число = {result}')

y1, y2 = map(float, input('Введите через пробел диапазон генерации случайного вещественного числа с двумя точками после запятой (y1, y2): ').split())

# Проверка на максимальное число (выстраиваем правильно диапазон чисел):
max_y = y2
if y1 > y2:
    y2 = y1
    y1 = max_y

now_sec = str(time.time())
rnd = int(now_sec[::-1][:3:])/1000
result_2 = y1 + rnd*(y2 - y1)

if int(str(result_2*1000//1)[:-2][-1:]) >= 5:
    result_2 = 0.01 + float(result_2//1) + float('0.' + str(result_2*100//1)[-4:][:2])
else:
    result_2 = float(result_2//1) + float('0.' + str(result_2*100//1)[-4:][:2])

# т.к. вещественное число может быть с множеством символов после запятой (а нам нужно ограничится двумя символами после запятой), то делаем ограничение кол-ва символов после запятой = 2
len_point = str(result_2).find('.') + 3
result_2 = str(result_2)[:len_point]

print(f'Случайное вещественное число = {result_2}')

z1, z2 = input("Введите через пробел диапазон генерации случайного символа (от \"a\" до \"z\"): ").split()

alphabet = st.ascii_lowercase

num1 = alphabet.find(z1)
num2 = alphabet.find(z2)

# Проверка на максимальное число (выстраиваем правильно диапазон):
max_num = num2
if num1 > num2:
    num2 = num1
    num1 = max_num

now_sec = str(time.time())
rnd = int(now_sec[::-1][:3:])/1000
result = num1 + rnd*(num2 - num1)

if int(str(result*1000//1)[:-2][1:]) >= 500:
    result = int(str(1 + result*1000//1000)[:-2])
else:
    result = int(str(result * 1000 // 1000)[:-2])

result_str = alphabet[result:][0]

print(f'Случайный символ = {result_str}')
