# -*- coding: utf-8 -*-
# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания
# первых трех уроков.


# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.
import cProfile

# start_num = int(input('Введите число: '))
new_num = 0

start_num = 123456789


def rek(a, b):
    num = a % 10
    a //= 10
    b *= 10
    b += num
    if a > 0:
        return rek(a, b)
    else:
        return b


# cProfile.run('rek(12345678945634524, 0)')
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #   9/1    0.000    0.000    0.000    0.000 1.py:15(rek)        rek(123456789, 0)
    #     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    #     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

    # 17/1    0.000    0.000    0.000    0.000 1.py:15(rek)         rek(12345678945634524, 0)

# 100 loops, best of 3: 1.13 usec per loop      12345
# 100 loops, best of 3: 2.2 usec per loop       1234567890
# 100 loops, best of 3: 3.57 usec per loop      123456789012345
# линейная сложность

# python -m timeit -n 100 -s "import one" "one.rek(123456789012345, 0)"


# resalt = rek(start_num, new_num)
# print(resalt)
