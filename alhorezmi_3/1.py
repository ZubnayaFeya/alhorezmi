# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

MIN_NUM = 2
MAX_NUM = 99
check_list = [2, 3, 4, 5, 6, 7, 8, 9]
one = [s for s in range(MIN_NUM, MAX_NUM + 1)]
count = 0
for i in check_list:
    for j in one:
        if j % i == 0:
            count += 1
            # break
    print(f'{i} - {count}')
    count = 0
