'''
6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
'''

# Решение:

import string as st

num1 = int(input("Введите номер буквы в алфавите (от 97 до 122): "))

str = chr(num1)
print(f'Решение методом № 1: Это буква \"{str}\"')

alphabet = st.ascii_lowercase
str = alphabet[num1 - 97]
print(f'Решение методом № 2: Это буква \"{str}\"')