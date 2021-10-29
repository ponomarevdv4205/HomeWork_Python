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

if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))
    print(currency_rates('1111111'))