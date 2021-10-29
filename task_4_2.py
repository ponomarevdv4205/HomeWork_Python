'''
Задание:
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

#Решение:
import requests
from decimal import Decimal

def currency_rates(currency):
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    url_set = requests.get(URL)
    content = url_set.content.decode(encoding=url_set.encoding)
    for eliment in content.split('<CharCode>')[1:]:
        currency_name = eliment[:3]
        value = (eliment.split('<Value>')[1:][0].split('</Value>')[0])
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        nominal = Decimal(eliment.split('<Nominal>')[1:][0].split('</Nominal>')[0])
        course = value / nominal
        if currency.upper() == currency_name:
            return course

print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('1111111'))