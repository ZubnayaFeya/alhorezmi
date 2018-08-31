# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint


LIMIT_LIST = 10
MAX_NUM = 100
MIN_NUM = 0
min_elem = 100
max_elem = 0
resalt = 0
one = [randint(MIN_NUM, MAX_NUM) for _ in range(LIMIT_LIST)]
two = one.copy()
for i, s in enumerate(one):
    if s > max_elem:
        max_elem = s
        ind_max = i
    elif s < min_elem:
        min_elem = s
        ind_min = i
if ind_min < ind_max and ind_max - ind_min > 0:  # можно было сократить условия используя сорт для полученных индексов.
    for i in one[ind_min + 1: ind_max]:
        resalt += i
elif ind_min > ind_max and ind_min - ind_max > 0:
    for i in one[ind_max + 1: ind_min]:
        resalt += i
print(resalt)
print(f'минимальный элемент - {min_elem} \nмаксимальный элемент {max_elem}')
print(one)
