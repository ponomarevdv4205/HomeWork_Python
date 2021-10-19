# Задание:

#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.

# Решение:

item = 1
my_list = []
total = 0         #сумма по заданию а
total_17 = 0    #сумма по заданию b, где добавляется фрагмент "17" к каждому элементу списка

while item <=1000:
    my_list.append(item**3)
    item +=2

print('Mой изначальный список такой: ' + str(my_list))

for i in range(0, len(my_list)):
    element_my_list = my_list[i]
    sum_element_my_list = 0

    while element_my_list != 0:
        last_figure =  element_my_list%10
        sum_element_my_list += last_figure
        element_my_list = element_my_list//10

    if not sum_element_my_list % 7:
        total += my_list[i]

    my_list[i] = int(str(my_list[i]) + '17')
    element_my_list = my_list[i]
    sum_element_my_list = 0

    while element_my_list != 0:
        last_figure =  element_my_list%10
        sum_element_my_list += last_figure
        element_my_list = element_my_list//10

    if not sum_element_my_list % 7:
        total_17 += my_list[i]

print('a) Cумма всех чисел из этого списка, сумма цифр которых делится нацело на 7 равна: ' + str(total))
print('Список с добавлением 17 к каждому элементу выглядит следующим образом: ' + str(my_list))
print('b) Cумма всех чисел из этого списка, сумма цифр которых делится нацело на 7 равна: ' + str(total_17))