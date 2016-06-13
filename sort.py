# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


array = [2, 23, 1, 4, 5, 34, 3, 52345, 56]


def bubble_sort(arr):
    """
    冒泡排序
    :param arr: 排序前的数组
    :return:排序后的数组
    """
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    print(array)


def insert_sort(arr):
    """
    插入排序：
    :param arr: 排序前的数组
    :return:排序后的数组
    """
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            i -= 1
    print(array)


def selection_sort(arr):
    """
    选择排序：
    :param arr: 排序前的数组
    :return:排序后的数组
    """
    for i in range(len(arr)):
        position = i
        for j in range(i,len(arr)):
            if arr[position] > arr[j]:
                position = j
        if position != i:
                tmp = arr[position]
                arr[position] = arr[i]
                arr[i] = tmp


if __name__ == "__main__":
    # bubble_sort(array)
    insert_sort(array)
