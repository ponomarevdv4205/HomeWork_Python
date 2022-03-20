'''
1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

# Решение:

num = int(input('Введите трехзначное число: '))

num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10

sum_result = num1 + num2 + num3
com_result = num1 * num2 * num3

print(f'Сумма трех цифр = {sum_result}')
print(f'Произведение трех цифр = {com_result}')
