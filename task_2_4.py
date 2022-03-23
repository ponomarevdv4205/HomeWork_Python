'''
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''

# Решение:

num = int(input('Введите количество элементов ряда (n): '))

print("Метод через цикл:")
if num > 0:
    rezult = 1
    rezult_str = 'Готовый ряд чисел: 1'
    for i in range(num - 1):
        rezult = rezult / -2
        rezult_str = rezult_str + ' ' + str(rezult)
    print(rezult_str)
else:
    print('Не верно введено n!')


def recursion(n, mno = 1):
    if n < 1:
        return ""
    return str(mno / -2) + " " + str(recursion(n-1, mno = mno / -2))

print("Метод через рекурсию:")
print(f'Готовый ряд чисел: 1 {recursion(num-1)}'[:-1])