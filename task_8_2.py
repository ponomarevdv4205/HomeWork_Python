'''
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''

# Решение:

from collections import Counter, deque

class My_Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(str):
    counter = Counter(str)
    item_sorted = deque(sorted(counter.items(), key=lambda item: item[1]))
    while len(item_sorted) > 1:
        weight = item_sorted[0][1] + item_sorted[1][1]
        node = My_Node(left=item_sorted.popleft()[0], right=item_sorted.popleft()[0])
        for i, item in enumerate(item_sorted):
            if weight > item[1]:
                continue
            else:
                item_sorted.insert(i, (node, weight))
                break
        else:
            item_sorted.append((node, weight))
    return item_sorted[0][0]

code_table = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, My_Node):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


str = input('Введите любую строку из трех слов: ')
haffman_code(haffman_tree(str))
print('Результат кодировки:')
for i in str:
    print(code_table[i], end='')
