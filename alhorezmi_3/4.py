# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint


LIMIT_LIST = 5
MAX_NUM = 1
MIN_NUM = 0
one = [randint(MIN_NUM, MAX_NUM) for _ in range(LIMIT_LIST)]
count = 1
count_max = 1

for i in range(len(one)):
    for j in range(i+1, len(one)):
        if one[i] == one[j]:
            count += 1
    if count > count_max:
        count_max = count
        num_max = one[i]
    count = 1
print(one)
print(num_max, count_max)
