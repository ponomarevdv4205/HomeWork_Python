'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

# Решение:

num1 = input('Введите последовательность чисел: ')
num2 = input('Введите какое число будем искать в этой последовательности: ')

rezult = 0

for item in num1:
    if item == num2:
        rezult += 1

print(f'В данной последовательности указанное число встречается {rezult} раз.')

