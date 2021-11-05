# Задание 6. Запись в файл bakery.csv

def write_records(sale):
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        if sale != 'end':
            file.write(f'{sale}\n')

user_input = ''
while user_input != 'end':
    user_input = input("python add_sale.py ")
    write_records(user_input)