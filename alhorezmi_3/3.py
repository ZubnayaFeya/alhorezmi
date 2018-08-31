# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint


LIMIT_LIST = 10
MAX_NUM = 100
MIN_NUM = 0
min_elem = 100
max_elem = 0
one = [randint(MIN_NUM, MAX_NUM) for _ in range(LIMIT_LIST)]
two = one.copy()
for i, s in enumerate(one):
    if s > max_elem:
        max_elem = s
        ind_max = i
    elif s < min_elem:
        min_elem = s
        ind_min = i
two[ind_min], two[ind_max] = max_elem, min_elem
print(f'минимальный элемент - {min_elem} \nмаксимальный элемент {max_elem}')
print(one)
print(two)