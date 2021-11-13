'''
Задание:
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
'''

# Решение:
from functools import wraps

def val_checker(lambda_func):
    def _logger(func):
        @wraps(func)
        def wrapper(x):
            if not lambda_func(x):
                raise ValueError(f'wrong val {x}')
            else:
                result = func(x)
            return result
        return wrapper
    return _logger

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(f'{calc_cube.__name__} - это имя исходной функции, т.е. декоратор замаскирован')
a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)