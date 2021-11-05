'''
Задание:
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''

#Решение:
import itertools, pickle

users = []
hobbys = []

with open('users.csv', 'r', encoding='utf-8') as file:
    for line in file:
        users.append(line.strip())

with open('hobby.csv', 'r', encoding='utf-8') as file:
    for line in file:
        hobbys.append(line.strip())

if len(users) < len(hobbys):
    exit(1)

users_hobby = {user: hobby for (user, hobby) in itertools.zip_longest(users, hobbys, fillvalue=None)}

with open('users_hobby.pickle', 'wb') as f:
    pickle.dump(users_hobby, f)

with open('users_hobby.pickle', 'rb') as f:
    content = pickle.load(f)

for item in content.items():
    print(item)
print(type(content))