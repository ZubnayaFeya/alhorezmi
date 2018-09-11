# -*- coding: utf-8 -*-
import sys

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


# def decorator_analize(func):
#
#     def wrap_analize(*args, **kwargs):
#         # name = func.__name__
#         result = func(*args, **kwargs)
#         for i in list(locals()):  # or globals():
#             print(i)
#         return func
#
#     return wrap_analize
#
#
# def _get_size(self, x):
#     total_mem = sys.getsizeof(x)
#
#     if hasattr(x, '__iter__'):
#         if hasattr(x, 'items'):
#             for y in x.items():
#                 total_mem += sys.getsizeof(y)
#         elif not isinstance(x, str):
#             for y in x:
#                 total_mem += sys.getsizeof(y)
#     return total_mem



MIN_NUM = 2
MAX_NUM = 99
result = {}
check_list = [2, 3, 4, 5, 6, 7, 8, 9]
one = [s for s in range(MIN_NUM, MAX_NUM + 1)]
count = 0
for i in check_list:
    for j in one:
        if j % i == 0:
            count += 1
            # break
    result[i] = count
    count = 0

for key, value in globals().copy().items():
    if not key.startswith('__'):
        count += sys.getsizeof(value)
        print(f'Переменная {key} занимает {sys.getsizeof(value)} места')
print(count)
