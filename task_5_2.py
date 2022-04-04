'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

# Решение:

from collections import deque

def sum_num(x, y):
    dict_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    step = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            num = dict_hex[x.pop()] + dict_hex[y.pop()] + step
        else:
            num = dict_hex[x.pop()] + step
        step = 0

        if num < 16:
            result.appendleft(dict_hex[num])
        else:
            result.appendleft(dict_hex[num - 16])
            step = 1

    if step:
        result.appendleft('1')

    return list(result)


def mult_num(x, y):
    dict_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    result_ = deque([deque() for i in range(len(y))])
    x, y = x.copy(), deque(y)
    step = 0

    for i in range(len(y)):
        num = dict_hex[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            result_[i].appendleft(num * dict_hex[x[j]])

        for s in range(i):
            result_[i].append(0)

    for c in range(len(result_[-1])):
        num = step

        for d in range(len(result_)):
            if result_[d]:
                num += result_[d].pop()

        if num < 16:
            result.appendleft(dict_hex[num])
        else:
            result.appendleft(dict_hex[num % 16])
            step = num // 16

    if step:
            result.appendleft(dict_hex[step])

    return list(result)


x = list(input('Введите 1-е шестнадцатиричное число: ').upper())
y = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print('-'*100)
print('Числа сохранены, как', x, 'и', y)
print('Результат сложения двух чисел:', sum_num(x, y))
print('Результат умножения двух чисел:', mult_num(x, y))
