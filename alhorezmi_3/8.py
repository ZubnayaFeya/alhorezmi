# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.
from random import randint


size = 4
matrix = [[int(input('input number: ')) for _ in range(size)] for _ in range(size)]
for line in matrix.copy():
    sum_ = 0
    for i in line:
        sum_ += i
        print(f'{i:>4}', end='')
    line.append(sum_)
    print(f'{line[-1]:>4}')

# в конце следует вывести матрицу, но так будет не красиво, а дублировать вышеописанный двойной цикл не логично.
print(matrix)
