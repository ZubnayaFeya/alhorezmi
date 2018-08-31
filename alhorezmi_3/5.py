# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint


LIMIT_LIST = 20
MAX_NUM = 100
MIN_NUM = -100
max_elem = -100
one = [randint(MIN_NUM, MAX_NUM) for _ in range(LIMIT_LIST)]
for i, s in enumerate(one):
    if 0 > s > max_elem:
        max_elem = s
        ind_max = i
print(one)
print(f'максимальный отрицательный элемент {max_elem}')
