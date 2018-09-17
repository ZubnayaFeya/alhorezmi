# 2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.
from collections import Counter as cou
# string = input('Введите строку для кодирования: ')


class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def walk(self, code, value):
        self.left.walk(code, value + '0')
        self.right.walk(code, value + '1')


def dict_sorted(data):
    c = cou()
    for i in data:
        c[i] += 1
    return c


def gen_gen(data):
    s = []
    for i in data.most_common():
        s.append(i)
    return s


def get_code(data):
    while len(data) >= 2:
        left_leaf = data.pop()
        right_leaf = data.pop()
        leaf_count = left_leaf[1] + right_leaf[1]
        data.append((MyNode(left=left_leaf[0], right=right_leaf[0]), leaf_count))
        data.sort(key=itemgetter(1), reverse=True)
    _node = data.pop()[0]
    code = {}
    _node.walk(code, '')
    print(code)
    for i in data:
        print(code[i], end=' ')


string = 'goloperedol bugaga'
a = dict_sorted(string)
print(list(a))
b = gen_gen(a)

for _ in range(len(b.copy()) - 1):
    i, j = b.pop()
    m, n = b.pop()
    p = MyNode('')
    p.left = MyNode(i)
    p.right = MyNode(m)
    b.append((p, j+n))
    b.sort(key=lambda tup: tup[1], reverse=True)

get_code(list(a))


# print(b)
print(p)
'''Ниже рабочий вариант. '''


# import heapq
# from collections import Counter
# from collections import namedtuple
#
#
# class Node(namedtuple("Node", ["left", "right"])):
#     def walk(self, code, acc):
#         self.left.walk(code, acc + "0")
#         self.right.walk(code, acc + "1")
#
#
# class Leaf(namedtuple("Leaf", ["char"])):
#     def walk(self, code, acc):
#         code[self.char] = acc or "0"
#
#
# def huffman_encode(s):
#     for ch, freq in Counter(s).items():
#         h.append((freq, len(h), Leaf(ch)))
#     heapq.heapify(h)
#     count = len(h)
#     while len(h) > 1:
#         freq1, _count1, left = heapq.heappop(h)
#         freq2, _count2, right = heapq.heappop(h)
#         heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
#         count += 1
#     code = {}
#     if h:
#         [(_freq, _count, root)] = h
#         root.walk(code, "")
#     return code
#
#
# def main():
#     s = 'goloperedol bugaga'
#     code = huffman_encode(s)
#     encoded = "".join(code[ch] for ch in s)
#     print(len(code), len(encoded))
#     for ch in sorted(code):
#         print("{}: {}".format(ch, code[ch]))
#     print(encoded)
#
#
# if __name__ == "__main__":
#     main()
