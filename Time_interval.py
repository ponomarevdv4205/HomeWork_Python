# Задание:
# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# Решение:

string_duration = input('Введите промежуток времени в секундах: ')

check_duration = False # проверка на число

while check_duration == False:
    while string_duration.isdigit() == False:
        print('Вы ввели не числовое значение! Повторите еще раз.')
        string_duration = input('Введите промежуток времени в секундах: ')
    duration = int(string_duration)
    if duration <= 0:
        print('Вы ввели недопустимое число (ниже или равно 0)! Повторите еще раз.')
        string_duration = input('Введите промежуток времени в секундах: ')
    else: check_duration = True

if (duration//60) < 1:
    second = duration
    print(str(second) + ' сек')
else:
    if (duration//3600) < 1:
        minute = duration//60
        second = duration - (minute*60)
        print(str(minute) + ' мин ' + str(second) + ' сек')
    else:
        if (duration//86400) < 1:
            hour = duration//3600
            minute = (duration - (hour*3600))//60
            second = duration - hour*3600 - minute*60
            print(str(hour) + ' час ' + str(minute) + ' мин ' + str(second) + ' сек')
        else:
            if(duration//86400) >= 1:
                day = duration//86400
                hour = (duration - day*86400)//3600
                minute = (duration - day*86400 - hour*3600)//60
                second = duration - day*86400 - hour*3600 - minute*60
                print(str(day) + ' дн ' +str(hour) + ' час ' + str(minute) + ' мин ' + str(second) + ' сек')