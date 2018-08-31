# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint


MAX_NUM = 200
MIN_NUM = 0
SIZE = 10
matrix = [[randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)] for _ in range(SIZE)]
minimal_lines = [250] * SIZE

for line in matrix:
    min_num = 0
    for i, num in enumerate(line):
        if num < minimal_lines[i]:
            minimal_lines[i] = num
        print(f'{num:>4}', end='')
    print('\n')

result = 0
for i in minimal_lines:
    if i > result:
        result = i
print(minimal_lines)
print(result)
