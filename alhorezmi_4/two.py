# -*- coding: utf-8 -*-
# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile


# С решетом Эратосфена
def erat(index):
    if index == 1:
        return 2
    limit = index ** 2
    sieve = [i for i in range(limit + 1)]
    sieve[1] = 0

    for i in range(2, limit + 1):
        if sieve[i] != 0:
            j = i * 2
            while j < limit:
                sieve[j] = 0
                j += i
    prime_nums = [i for i in sieve if i != 0]
    return prime_nums[index - 1]

# cProfile.run('erat(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 two.py:12(<listcomp>)
#         1    0.000    0.000    0.000    0.000 two.py:21(<listcomp>)
#         1    0.000    0.000    0.000    0.000 two.py:8(erat)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 100 loops, best of 3: 5.56 usec per loop  5
# 100 loops, best of 3: 22.2 usec per loop  10
# 100 loops, best of 3: 50.2 usec per loop  15
# 100 loops, best of 3: 92 usec per loop    20
# o(4n)


def gen():
    val = 1
    while True:
       val += 1
       yield val


def is_simple(num):
    list_ = [s for s in range(2, num)]
    for i in list_:
        if num % i == 0:
            return 0
    return num


def ne_erat(index):
    num_list = []
    gen_num = gen()
    while len(num_list) < index:
        num = next(gen_num)
        if is_simple(num) == num:
            num_list.append(num)
    return num_list[-1]

# cProfile.run('ne_erat(6)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        13    0.000    0.000    0.000    0.000 two.py:33(gen)
#        12    0.000    0.000    0.000    0.000 two.py:40(is_simple)
#        12    0.000    0.000    0.000    0.000 two.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 two.py:48(ne_erat)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        13    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        12    0.000    0.000    0.000    0.000 {built-in method builtins.next}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 100 loops, best of 3: 9.7 usec per loop   5
# 100 loops, best of 3: 40 usec per loop    10
# 100 loops, best of 3: 87.8 usec per loop  15
# 100 loops, best of 3: 173 usec per loop   20
# o(4n)
