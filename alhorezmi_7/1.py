# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
from random import shuffle, randint


def bubble(func):
    def wrap_bubble(*args, **kwargs):
        array = func(*args, **kwargs)
        n = 1
        count = 0
        while n < len(array):
            for i in range(len(array) - n):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i +1], array[i]
                    count += 1
            if count == 0:
                break
            n += 1
            count = 0
            # print(array)
        return array
    return wrap_bubble

@bubble
def gen_full_list(begining=-100, ending=100):
    random_list = [s for s in range(begining, ending)]
    shuffle(random_list)
    print(random_list)
    return random_list


@bubble
def gen_list(begining=-100, ending=99):
    it = randint(3, ending)
    # если я правильно понял то списое это случайное количество чисел из заданного диапазона
    random_list = [randint(begining, ending) for _ in range(it)]
    shuffle(random_list)
    print(it)
    print(random_list)
    return random_list


# print(gen_list(-5, 5))
print(gen_list())


# def wrap_bubble(array):
#     n = 1
#     count = 0
#     while n < len(array):
#         for i in range(len(array) - n):
#             if array[i] < array[i + 1]:
#                 array[i], array[i + 1] = array[i +1], array[i]
#                 count += 1
#         if count == 0:
#             break
#         n += 1
#         count = 0
#         # print(array)
#     return array
