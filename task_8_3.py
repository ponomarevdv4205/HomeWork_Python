'''
Задание:
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

# Решение:
from functools import wraps

'''
Это код без маскировки:
def type_logger(func):
    def log_func(*args, **kwargs):
        result = {'name_fun': func.__name__}
        if args:
            print(type(args))
            for i in args:
                result[i] = type(i)
        if kwargs:
            print(type(kwargs))
            for i in kwargs.values():
                result[i] = type(i)
        return result
    return log_func
'''

#Это код с маскировкой:
def type_logger(func):
    @wraps(func)
    def log_func(*args, **kwargs):
        result = {'name_fun': func.__name__}
        if args:
            print(type(args))
            for i in args:
                result[i] = type(i)
        if kwargs:
            print(type(kwargs))
            for i in kwargs.values():
                result[i] = type(i)
        return result
    return log_func

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(a = 5, b = 'my_example')
#a = calc_cube(5, 'my_example')
print(f'{calc_cube.__name__} - это имя исходной функции, т.е. декоратор замаскирован')
str_result = ""
flag_name = True
for k, v in a.items():
    if flag_name:
        flag_name = False
    else:
        str_result = str_result + f'{k}: {v}, '

print(f'{a["name_fun"]}({str_result[:-2]})')