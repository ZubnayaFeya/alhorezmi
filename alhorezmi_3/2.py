# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
from random import randint


LIMIT_LIST = 100
MIN_NUM = 0
MAX_NUM = 100
one = [randint(MIN_NUM, MAX_NUM) for _ in range(LIMIT_LIST)]
two = []
for i, s in enumerate(one):
    if s % 2 != 1:
        two.append(i)
print(*one)
print(*two)
