'''
5.	Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''

# Решение:

import string as st

str1, str2 = input("Введите через пробел две буквы (от \"a\" до \"z\"): ").split()

alphabet = st.ascii_lowercase

num1 = ord(str1) - 97 + 1
num2 = ord(str2) - 97 + 1

print(f'Буква \"{str1}\" находится на позиции {num1}')
print(f'Буква \"{str2}\" находится на позиции {num2}')

max_num = num2
if num1 > num2:
    num2 = num1
    num1 = max_num

between = num2 - num1 - 1

print(f'Между ними находится {between} букв')
