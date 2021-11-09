'''
Задание:
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
'''

#Решение:
import shutil
import os
import pathlib

dir_name_str = str(os.getcwd()) + "/my_project/templates"
dir_name = pathlib.Path(dir_name_str)
dir_name.mkdir(parents=True, exist_ok=True)

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    flag_copy = True
    if filenames:
        for item in filenames:
            if item[-5:] != '.html':
                flag_copy = False
        if flag_copy == True:
            os.chdir(dirpath)
            os.chdir('..')
            dirpath = os.getcwd()
            shutil.copytree(dirpath, dir_name, dirs_exist_ok=True)

print("Готово! Смотри каталог my_project")