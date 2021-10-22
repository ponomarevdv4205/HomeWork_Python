'''
Задание:
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
'''

#Решение:

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'Изначальный список был: {my_list}')
new_my_list =[]

for element_list in my_list:
    if element_list.isdigit() == True:
        new_my_list.append('"')
        if int(element_list) // 10 < 1:
            element_list = '0' + element_list
        new_my_list.append(element_list)
        new_my_list.append('"')
    elif (element_list[0] == '+' or element_list[0] == '-') and (element_list[1:].isdigit() == True):
        new_my_list.append('"')
        if int(element_list[1:]) // 10 < 1:
            element_list = element_list[0] + "0" + element_list[1:]
        new_my_list.append(element_list)
        new_my_list.append('"')
    else:
        new_my_list.append(element_list)

print(f'Новый список стал: {new_my_list}')

print_new_my_list = "" #начальный текст итогового результата
ind_element = 0 #начальный индекс итогового списка
flag_marks = True #установка флага на кавычки

for element_list in new_my_list:
    if element_list != '"' and ind_element != len(new_my_list) - 1 and flag_marks == True:
        print_new_my_list = print_new_my_list + element_list + " "
    elif element_list == '"' and ind_element != len(new_my_list) - 1 and flag_marks == True:
        print_new_my_list = print_new_my_list + element_list
        flag_marks = False
    elif element_list == '"' and ind_element != len(new_my_list) - 1 and flag_marks == False:
        print_new_my_list = print_new_my_list + element_list + " "
        flag_marks = True
    else:
        print_new_my_list = print_new_my_list + element_list
    ind_element += 1

print(f'Результат: {print_new_my_list}')