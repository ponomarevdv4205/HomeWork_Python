'''
Задание:
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки.
Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
'''
#Решение:

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(f'Изначальный список был: {my_list}')

for element_list in my_list:
    name = ''
    flag_whitespace = False  # флаг на встречу пробела
    for item_element in range(len(element_list), 0, -1):
        if str(element_list[item_element - 1]) != ' ' and flag_whitespace == False:
            name = name + str(element_list[item_element - 1])
        else:
            flag_whitespace = True
    name = name[::-1].lower()
    name = name[0].upper()  + name[1:]
    print(f'Привет, {name}!')