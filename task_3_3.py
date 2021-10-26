'''
Задание:
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён,
а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
'''

#Решение:

name = ['Иван', 'Мария', 'Петр', 'Илья', 'Дмитрий', 'Валерий', 'Денис', 'Петр', 'Артур', 'Алина', 'Алина']

def thesaurus(*args):
    names = []
    dictionary_names = {}

    # Создаем не повторяющиеся ключи (сразу сортированные по алфовиту)
    for item in args:
        names.append(item[0])
    names = list(set(names))
    names.sort()

    # Заполняем словарь
    args = set(args) # Убираем дубликаты имен
    for item_names in names:
        for item_args in args:
            if item_args[0] == item_names:
                dictionary_names.setdefault(item_names, []).append(item_args)
    return dictionary_names

print(thesaurus(*name))