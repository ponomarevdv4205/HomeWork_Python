'''
Задание:
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
'''

# Решение:

def my_fun(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            yield i

n = int(input("Введите число n для создания генератора нечётных чисел: "))
print(f">>> odd_to_{n} = odd_nums({n})")
for item in my_fun(n):
    print(f">>> next(odd_to_{n})")
    print(str(item) + "")
print(f"...StopIteration...")