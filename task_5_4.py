'''
Задание:
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```

Подсказка: использовать возможности python, изученные на уроке.
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
'''

# Решение:
import time, sys

def my_fun1(src):
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
            yield src[i]

def my_fun2(src):
    len_src = len(src)
    while len_src != 0:
        if src[len_src - 1] <= src[len_src - 2]:
            del src[len_src - 1]
        len_src -= 1
    del src[0]
    yield src


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(f'Первый вариант решения занял памяти: {sys.getsizeof(my_fun1(src))} байт')
print(f'Исходный список: {src}')
start_time = time.perf_counter_ns()
print(f'Результат: {list(my_fun1(src))}')
end_time = time.perf_counter_ns()
print(type(my_fun1(src)))
print("Первый вариант решения занял времени: %s наносекунд" % (end_time - start_time))
print("-"*100)
print(f'Второй вариант решения занял памяти: {sys.getsizeof(my_fun2(src)) + 28} байт') # +28 байт это переменная len_src в функции
print(f'Исходный список: {src}')
start_time = time.perf_counter_ns()
print(f'Результат: {list(my_fun2(src))[0]}')
end_time = time.perf_counter_ns()
print(type(my_fun2(src)))
print("Второй вариант решения занял времени: %s наносекунд" % (end_time - start_time))