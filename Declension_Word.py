# Задание:
# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

# Решение:

counter = 1
percent_1 = ' процентов'
percent_2 = ' процент'
percent_3 = ' процента'

while counter <= 100:
    if counter>=0:
        if counter%100>=10 and counter%100<=20:
            print(str(counter) + percent_1)
        elif counter%10==1:
            print(str(counter) + percent_2)
        elif counter%10>=2 and counter%10<=4:
            print(str(counter) + percent_3)
        else:
            print(str(counter) + percent_1)
    counter += 1