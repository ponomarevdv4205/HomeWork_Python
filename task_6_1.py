'''
Задание:
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

# Решение:
import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = response.content.decode(encoding=response.encoding)

file = open('nginx_logs.txt', 'w')
file.writelines(content)

result = []
items = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_open:
    for idx, item in enumerate(file_open):
        item_whitespace = item.split()
        items = [item_whitespace[0], item_whitespace[5][1:], item_whitespace[6]]
        result.append(tuple(items))
        if idx == 10: #если просмотреть весь файл, то нужно поставить: if idx == len(content)-1:
            break
print(result)

#Дополнительно записываю результат в файл, чтобы увидеть, что весь объем исходного файла обработался:
with open('result_nginx_logs.txt', 'w') as file_result:
    for i in range(len(result)):
        file_result.writelines(f'{result[i]}\n')