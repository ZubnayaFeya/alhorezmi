# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
from random import randint


LIMIT_LIST = 10
MAX_NUM = 10
MIN_NUM = 0
min_elem = 100
min2_elem = 100
one = [randint(MIN_NUM, MAX_NUM) for _ in range(LIMIT_LIST)]
for s in one:
    if s < min_elem and min_elem <= min2_elem:
        min_elem, min2_elem = s, min_elem
    elif s >= min_elem and s < min2_elem:
        min2_elem = s
print(f'минимальный элемент - {min_elem} \nминимальный2 элемент {min2_elem}')
print(one)
