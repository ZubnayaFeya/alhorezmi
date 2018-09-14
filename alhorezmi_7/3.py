# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
# другой – не больше ее.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.
from random import shuffle, randint


def gen_list(begining=1, ending=50):
    m = randint(3, ending)
    it = 2 * m + 1
    random_list = [randint(begining) for _ in range(it)]
    shuffle(random_list)
    print(it)
    print(random_list)
    return random_list


array = gen_list()
count_min = 0
count_max = 0

for i in range(array):
    for j in range(array):
        if i == j:
            continue
        else:
            if j > i:
                count_max += 1
            elif j < i:
                count_min += 1
    if count_min == count_max:
        print(i)
    else:
        print('нет единого элемента являющегося медианой')

# во втором варианте я бы сделал масив уникальных чисел и там бы последний элс был бы не нужен.
# так же имеется вариант с рекурсией, но не успел сваять.

