'''
Задание:
5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''

# Решение:

def my_fun1(src):
    for i in range(len(src)):
        flag_repetitions = False
        for idx, item_comparison in enumerate(src):
            if src[i] == item_comparison and idx != i:
                flag_repetitions = True
        if flag_repetitions == False:
            yield src[i]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(list(my_fun1(src)))
print(type(my_fun1(src)))
