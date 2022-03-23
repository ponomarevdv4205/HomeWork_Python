'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
'''

# Решение:

str = input("Введите через пробел несколько натуральных чисел: ")

number = ''
number_sum = 0

for item in str.split():
    sum = 0
    for i in item:
        sum = sum + int(i)
    if sum > number_sum:
        number = item
        number_sum = sum

print(f'Число с наибольшей суммой числел: {number}, а сумма его цифр = {number_sum}')