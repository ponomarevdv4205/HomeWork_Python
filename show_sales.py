# Задание 6. Чтение из файла bakery.csv

def reading_records(start, end):
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        if start == 0 and end == 0:
            lines = file.read()
            return lines
        elif end == 0:
            lines = file.readlines()[start - 1:]
            for item in lines:
                print(item.replace('\n', ''))
        else:
            lines = file.readlines()[start - 1:end]
            for item in lines:
                print(item.replace('\n', ''))

user_input = input("python show_sales.py ").split()
if len(user_input) == 0:
    print(reading_records(0, 0))
elif len(user_input) == 1:
    reading_records(int(user_input[0]), 0)
elif len(user_input) == 2:
    reading_records(int(user_input[0]), int(user_input[1]))
else:
    print("Вы ввели не правильные параметры чтения файла. Повторите заново")