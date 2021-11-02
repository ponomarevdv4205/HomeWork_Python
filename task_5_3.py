'''
Задание:
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
'''

# Решение:

def func2(func, tutors, klasses):
    for i in range(len(tutors)):
        if i <= len(klasses)-1:
            print(list(func(tutors, klasses))[i])
            yield func(tutors,klasses)[i]
        else:
            klasses.append(None)
            print(list(func(tutors, klasses))[i])
            yield func(tutors, klasses)[i]

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '7В']

list(func2(lambda x,y: list(zip(x,y)), tutors, klasses))
print(type(func2(lambda x,y: list(zip(x,y)), tutors, klasses)))
