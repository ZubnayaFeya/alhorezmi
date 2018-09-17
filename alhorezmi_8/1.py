# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. Для решения
# задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib.
from hashlib import sha1


string = input('Введите строку: ')

str_len = len(string)
MIN_LEN = 1
all_str = []

while str_len > 1:
    for i in range(str_len):
        sub = sha1(string[i:i + MIN_LEN].encode('utf-8')).hexdigest()
        if sub not in all_str:
            all_str.append(sub)
    MIN_LEN += 1
    str_len -= 1
print(f'В строке "{string}" {len(all_str)} подстрок')
