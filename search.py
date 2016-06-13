# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'
import math
array = [1, 23, 25, 41, 55, 134, 333, 523, 5656]


def dig_search(arr, key):
    start = 0
    end = len(arr)-1

    while start < end:
        mid = start + math.ceil((end-start)/2)
        print(arr[mid],mid)
        if key > arr[mid]:
            start = mid+1
            continue
        elif key < arr[mid]:
            end = mid-1
            continue
        elif key == arr[mid]:
            print(mid+1)
            return mid
    print('not find')

if __name__ == '__main__':
    dig_search(array, 41)
