# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


array = [2, 23, 1, 4, 5, 34, 3, 52345, 56]


def bubble_sort(arr):
    """
    冒泡排序
    :param array: 排序前的数组
    :return:排序后的数组
    """
    n = len(array)
    for i in range(0, n):
        for j in range(i+1, n):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    print(array)


def insert_sort(arr):
    """
    插入排序：
    :param array: 排序前的数组
    :return:排序后的数组
    """
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        for j in range(i-1, array[j+1] < array[j], -1):
            # if array[j+1] < array[j]:
            array[j+1] = array[j]
            array[j] = temp
            # else:
            #     break
    print(array)


if __name__ == "__main__":
    # bubble_sort(array)
    insert_sort(array)
