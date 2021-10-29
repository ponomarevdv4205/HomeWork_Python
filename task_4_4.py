'''
Задание:
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
'''

#Решение:
import utils

print(f"Курс валюты GBP = {utils.currency_rates('GBP')}")
print(f"Курс валюты BRL = {utils.currency_rates('BRL')}")
print(f"Курс валюты CNY = {utils.currency_rates('CNY')}")