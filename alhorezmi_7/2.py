# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import uniform, randint, shuffle


def gen_list(begining=0, ending=49):
    it = randint(3, ending)
    # если я правильно понял то списое это случайное количество чисел из заданного диапазона
    random_list = [uniform(begining, ending) for _ in range(it)]
    shuffle(random_list)
    print(f'всего в массиве {it} чисел')
    return random_list


def merge_sort(array):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    first = merge_sort(array[:middle])
    second = merge_sort(array[middle:])
    return _merge(first, second)


def _merge(first, second):
    sorted_list = []
    while first and second:
        if first[0] < second[0]:
            sorted_list.append(first.pop(0))
        else:
            sorted_list.append(second.pop(0))
    if first:
        sorted_list.extend(first)
    if second:
        sorted_list.extend(second)
    return sorted_list


if __name__ == '__main__':
    unsorted_array = gen_list()
    sorted_array = merge_sort(unsorted_array)
    print('unsorted:', unsorted_array)
    print('sorted:  ', sorted_array)
