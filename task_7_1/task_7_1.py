'''
Задание:
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
'''

# Решение:
import os
import pathlib

def my_fun(my_dict):
    path_abs = os.getcwd()
    for key, value in my_dict.items():
        dir_name_str = os.path.join(os.getcwd(), key)
        dir_name = pathlib.Path(dir_name_str)
        if type(key) == str:
            if key.find('.') == - 1:
                dir_name.mkdir(parents=True, exist_ok=True)
            else:
                file = open(dir_name, 'w')
                file.close()
        if type(value) == dict:
            os.chdir(dir_name_str+'/')
            my_fun(value)
            os.chdir('..')
        else:
            if type(value) != str:
                os.chdir(dir_name_str + '/')
                for item in value:
                    dir_name_str = os.path.join(os.getcwd(), item)
                    dir_name = pathlib.Path(dir_name_str)
                    if item.find('.') == - 1:
                        dir_name.mkdir(parents=True, exist_ok=True)
                    else:
                        file = open(dir_name, 'w')
                        file.close()
                os.chdir('..')
            else:
                os.chdir(dir_name_str + '/')
                dir_name_str = os.path.join(os.getcwd(), value)
                dir_name = pathlib.Path(dir_name_str)
                if value.find('.') == - 1:
                    dir_name.mkdir(parents=True, exist_ok=True)
                else:
                    file = open(dir_name, 'w')
                    file.close()
                os.chdir('..')
    os.chdir(path_abs)

my_discount_1 = {'my_project_1':('settings', 'mainapp', 'adminapp', 'authapp')}
my_discount_2 = {'my_project_2':{'settings':{}, 'mainapp':{'mainapp_2':{'mainapp_22', 'file_mainapp_22.txt'}}, 'adminapp':'end_adminapp', 'authapp':{'authapp_2', 'authapp_22'}}}
my_discount_3 = {'my_project_3':{'settings':{}, 'mainapp':{'mainapp_2':{'mainapp_3':{'file_mainapp_31.txt','file_mainapp_32.txt'}}}, 'adminapp':'end_adminapp', 'authapp':{'authapp_22':'end_authapp_2'}}}
#Создаем структуру каталогов при помощи словаря (сделал более сложную структуру каталогов, чем в задании, с созданием подкаталогов и файлов)
my_fun(my_discount_1)
my_fun(my_discount_2)
my_fun(my_discount_3)
print("Каталоги и файлы созданы (в трех различных вариантах папок проектов)!")