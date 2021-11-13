'''
Задание:
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''

#Решение:
import re

RE_EMAIL_USERNAME = re.compile(r'\b(\w*)@\b')
RE_EMAIL_DOMAIN= re.compile(r'@(\w*\.\w*)\b')

def email_parse(email_address):
    result = {'username': '', 'domain': ''}
    if not RE_EMAIL_USERNAME.findall(email_address):
        raise ValueError('wrong email: {}'.format(email_address))
    else: result['username'] = RE_EMAIL_USERNAME.findall(email_address)[0]
    if not RE_EMAIL_DOMAIN.findall(email_address):
        raise ValueError('wrong email: {}'.format(email_address))
    else: result['domain'] = RE_EMAIL_DOMAIN.findall(email_address)[0]
    return result

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))