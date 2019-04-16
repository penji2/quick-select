import matplotlib.pyplot as plt
import random
import sys
import numpy as np

sys.setrecursionlimit(10000)


def get_random_table(length_of_table, max_number):
    random_table = random.sample(range(1, max_number), length_of_table)
    return random_table


def swap(array, a, b):
    if a > len(array) - 1 or b > len(array) - 1:
        print(array)
        print("w funkcji swap: a", a, "b", b)
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
    return array


def divide(array, left, right, pivot_index, comparisons):
    swap(array, pivot_index, left)
    divide_index = left
    for i in range(left + 1, right + 1):
        if array[i] < array[left]:
            divide_index += 1
            swap(array, divide_index, i)
    swap(array, divide_index, left)
    return divide_index, comparisons


# quick_select returns a k'th smallest value from array
def quick_select(array, left, right, k, comparisons):
    if left == right:
        return array[left], comparisons
    pivot_index = random.randrange(left, right)
    comparisons += 1
    temp, comparisons = divide(array, left, right, pivot_index, comparisons)
    if k == temp:
        return array[temp], comparisons
    elif k < temp:
        return quick_select(array, left, temp - 1, k, comparisons)
    else:
        if temp == right:
            return quick_select(array, left, right, k, comparisons)
        else:
            return quick_select(array, temp + 1, right, k, comparisons)


def plot_number_of_comparison_in_function_of_table_length(start, stop, step):
    table_of_comparisons = []
    xaxis = []
    comparisons = 0
    k = random.randrange(start - 1)
    for i in range(start, stop + 10, step):
        comparisons = quick_select(get_random_table(i, i*5), 0, i - 1, k, comparisons)[1]
        table_of_comparisons.append(comparisons)
        xaxis.append(i)
    # plt.plot(xaxis, table_of_comparisons)
    # plt.title('Wykres zależności liczby porównań w funkcji długości tablicy')
    # plt.ylabel('liczba porównań')
    # plt.xlabel('długość tablicy')
    # plt.grid(linestyle='--')
    # plt.show()
    return table_of_comparisons, xaxis

def plot_average(start, stop, step, for_average):
    y = np.zeros(stop//step)
    xaxis = plot_number_of_comparison_in_function_of_table_length(start, stop, step)[1]
    for i in range(for_average):
        y = y + np.array(plot_number_of_comparison_in_function_of_table_length(start, stop, step)[0])
    plt.plot(xaxis, y/for_average)
    plt.title('Wykres zależności sredniej liczby porównań w funkcji długości tablicy')
    plt.ylabel('liczba porównań')
    plt.xlabel('długość tablicy')
    plt.grid(linestyle='--')
    plt.show()


def testing():
    k = 4  # k'th smallest element
    # array = [4, 9, 6, 2, 1]
    # print('Dostałem taka tablice: ', array)
    # print(k + 1, "-ty najmniejszy element: ", quick_select(array, 0, len(array) - 1, k, 1))

    # plot_number_of_comparison_in_function_of_table_length(10, 100, 1)
    i = 10
    array = get_random_table(i, i+5)
    print(k+1, "najmniejszy", quick_select(array, 0, i - 1, k, 0))
    print(array)

def main():
    start = 10
    stop = 1100
    step = 10
    for_average = 50
    #  plot_number_of_comparison_in_function_of_table_length(start, stop, step)
    #  plot_average(start, stop, step, for_average)
    testing()


main()

