'''
Задание:
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
 а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''

#Решение:
import os

def max_len(dir_name, max = 0):
    '''Функция по определению максимального размера файла'''
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for item_files in filenames:
            dir_file_str = str(dirpath) + '/' + str(item_files)
            len_item_files = os.stat(dir_file_str).st_size
            if len_item_files > max:
                max = len_item_files
    return max

def my_result(dir_name, result):
    '''Функция по заполнению словаря результатами подсчёта'''
    for key in result.keys():
        result[key] = 0
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for item_files in filenames:
            dir_file_str = str(dirpath) + '/' + str(item_files)
            len_item_files = os.stat(dir_file_str).st_size
            for key, item in result.items():
                if len_item_files <= key:
                    result[key] = item + 1
                    break
    return result

result = {}
os.chdir('some_data')
dir_name = os.getcwd()

if (max_len(dir_name)**(1/10)) % 1 > 0:
    if int(str(max_len(dir_name))[0]) >=5:
        quantity_key = int(3 + (max_len(dir_name)**(1/10)) // 1)
    else:
        quantity_key = int(4 + (max_len(dir_name) ** (1 / 10)) // 1)
else:
    if int(str(max_len(dir_name))[0]) >= 5:
        quantity_key = 2 + int((max_len(dir_name) ** (1 / 10)) // 1)
    else:
        quantity_key = int(3 + (max_len(dir_name) ** (1 / 10)) // 1)

for i in range(1, quantity_key):
    key = 10 ** i
    result.setdefault(key, 0)

result_del =[]
for key, value in my_result(dir_name, result).items():
    if value == 0:
        result_del.append(key)
for i in result_del:
    del result[i]
print(result)