'''
Задание:
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
'''

#Решение:
import random

def get_jokes(n):
    '''Функция get_jokes(n) принимает число n и возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):'''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result_dictionary = []
    items_nouns = []
    items_adverbs = []
    items_adjectives = []

    if n > 0 and n <= 5:

       def item_completion(list_name, items_name):
           '''Функция item_completion(list_name, items_name) принимает полный список слов и имя списка к случайному заполнению этими словами без повторений с использованием флага'''
           items_name.append(random.choice(list_name))
           for item in range(n - 1):
               flag_replay = True
               while flag_replay == True:
                   item_rnd = random.choice(list_name)
                   for item_items_name in items_name:
                       if item_items_name != item_rnd:
                           flag_replay = False
                       else:
                           flag_replay = True
                           break
                   if flag_replay == False:
                       items_name.append(item_rnd)
           return items_name

       items_nouns = item_completion(nouns, items_nouns)
       items_adverbs = item_completion(adverbs, items_adverbs)
       items_adjectives = item_completion(adjectives, items_adjectives)
       for idx in range(n):
           result_dictionary.append(f'{items_nouns[idx]} {items_adverbs[idx]} {items_adjectives[idx]}')
       return result_dictionary

    elif n > 5:
        return "Вы ввели более 5 шуток, что не допустимо."
    else: return "Вы ввели 0 или меньше шуток, поэтому результат нулевой."

get_jokes_result = get_jokes(int(input('Введите число n нужных шуток (от 0 до 5): ')))
print(get_jokes.__doc__)
print(get_jokes_result)