'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

# Решение:

num = input('Введите натуральное число: ')
rezult = ''
for item in range(len(num) - 1, -1, -1):
    rezult = rezult + num[item]
print(f'Число в обратную сторону (метод через range): {rezult}')

rezult = ''
for idx, item in enumerate(num):
    rezult = item + rezult
print(f'Число в обратную сторону (метод через enumerate): {rezult}')

def recursion(n):
    if len(n) < 1:
        return n
    return n[-1] + recursion(n[:-1])

print(f'Число в обратную сторону (метод через рекурсию): {recursion(num)}')