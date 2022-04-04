'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''

# Решение:

import collections

company_kol = int(input('Введите количество предприятий: '))

company_list = []
for i in range(company_kol):
    company_list.append(input(f'Введите имя предприятия № {i+1} (без знаков препинания, цифр и спецсимволов): '))

Company = collections.namedtuple('Company', company_list)

company_date = []
for i in range(company_kol):
    company_date.append(input(f'Введите через пробел прибыль за 4 квартала (т.е. 4 отдельных числа) предприятия № {i+1}: '))

data_tuple = Company._make(company_date)
print('-'*200)

year_sum = []
for i in range(company_kol):
    year_data = list(data_tuple[i].split())
    year_sum.append(sum(float(i) for i in year_data))

average_sum = sum(i for i in year_sum)/company_kol

company_min = []
company_max = []
for i in range(company_kol):
    if year_sum[i] < average_sum:
        company_min.append(data_tuple._fields[i])
    else:
        company_max.append(data_tuple._fields[i])

print(f'Средняя годовая прибыль по всем предприятиям равна {average_sum}')
print('Список предприятий, прибыль которых меньше средней:', ', '.join(company_min))
print('Список предприятий, прибыль которых больне или равна средней:', ', '.join(company_max))
