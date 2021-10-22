'''
Задание:
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

#Решение:
price_list = [57.8, 46.51, 97, 46.44, 1.04, 478.00, 77.4, 15.55, 47, 6.04, 58.44, 2.99, 52.07, 19.78, 10]
print(f'Изначальный список цен был таким: {price_list}')

for idx, element_price_list in enumerate(price_list, start=0):
    num_symbol = int(str(element_price_list).find('.'))
    name_after = ''
    if num_symbol == -1:
        name_after = '00'
        name_element = str(element_price_list) + '.' + name_after
    else:
        if len(str(element_price_list)[num_symbol+1:]) == 1:
            name_after = str(element_price_list)[num_symbol+1:] + '0'
        elif len(str(element_price_list)[num_symbol+1:]) == 0:
            name_after = str(element_price_list)[num_symbol+1:] + '00'
        else:
            name_after = str(element_price_list)[num_symbol+1:]
        name_element = str(element_price_list)[:num_symbol] + '.' + name_after
    price_list[idx] = name_element

name_element = ''
for element_price_list in price_list:
    num_symbol = int(str(element_price_list).find('.'))
    name_element = name_element + str(element_price_list)[:num_symbol] + ' руб ' + str(element_price_list)[num_symbol + 1:] + ' коп, '
name_element = name_element[::-1][2:][::-1]
print(f'Изначальный список в одну строку: {name_element}')

for idx, element_price_list in enumerate(price_list, start=0):
    price_list[idx] = float(element_price_list)
print(f'Цены изначального списка, отсортированные по возрастанию: {sorted(price_list)}')

#Докозательство, что объект списка после сортировки остался тот же:
remained_same = True
len_list = len(price_list)
for number in price_list[:]:
    if number in sorted(price_list):
        remained_same = True
        len_list -= 1
    else:
        remained_same = False
if remained_same == True and len_list == 0:
    print("Т.к. все элементы изначального списка встречаются в отсортированном списке по одному разу, то объект списка после сортировки остался тот же")
else:
    print("Т.к. все элементы изначального списка встречаются в отсортированном списке не по одному разу, то объект списка после сортировки не остался тем же")

new_price_list = sorted(price_list, reverse = True)
print(f'Цены списка (новый), отсортированные по убыванию: {new_price_list}')
print(f'Цены пяти самых дорогих товаров, отсортированные по возрастанию: {sorted(price_list, reverse = True)[:5][::-1]}')