# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


def solution(number):
    """
    Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
    :param number:
    :return:summary
    """
    summary = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            summary += i
    return summary


def my_parse_int(string1):
    string1=string1.strip()
    for i in range (0, len(string1)):
        if num(string1[i])==False:
            return 'NaN'
    return int(string1)

def num(str):
    list = '0123456789'
    for i in range(0,len(list)):
        if str == list[i]:
            return True
    return False


def my_parse_int1(string1):
    string1=string1.strip()
    for i in range(0, len(string1)):
        if num(string1[i])==False:
            return 'NaN'
    return int(string1)


def diamond(n):
    """
    Give me Diamond
    :param n:
    :return:diamond_str
    """
    if n % 2 == 0:
        return
    count = 1
    diamond_str = ''
    while count < n+1:
        for i in range(0, n/2-count/2):
            diamond_str += ' '
        for i in range(0,count):
            diamond_str += '*'
        diamond_str += '\n'
        count += 2
    count = n-2
    while count > 0:
        for i in range(0, n/2-count/2):
            diamond_str += ' '
        for i in range(0, count):
            diamond_str += '*'
        diamond_str += '\n'
        count -= 2
    return diamond_str

if __name__ == '__main__':
    diamond(5)
