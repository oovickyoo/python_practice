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


def dig_pow(n, p):
    """
    Playing with digits
    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    If it is the case we will return k, if not return -1.
    :param n:
    :param p:
    :return:
    """
    s = str(n)
    x = 0
    for i in range(0, len(s)):
        x += int(s[i]) ** (p+i)
    return x/n if x % n == 0 else -1


def diamond(n):
    """
    Give me Diamond
    :param n:
    :return:diamond_str
    """
    if n % 2 == 0 or n < 0:
        return
    count = 1
    diamond_str = ''
    while count < n+1:
        for i in range(0, n/2-count/2):
            diamond_str += ' '
        for i in range(0, count):
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


def unique_in_order(iterable):
    """
    Unique In Order
    对输入的序列去重后输出
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order([1,2,2,3,3])       == [1,2,3]
    :param iterable:
    :return:
    """
    uni_list=[]
    if len(iterable) == 0:
        return uni_list
    uni_list.append(iterable[0])
    for i in range(1, len(iterable)):
        if iterable[i] != uni_list[-1]:
            uni_list.append(iterable[i])
    return uni_list


def longest_consec(strarr, k):
    """
    Consecutive strings
    You are given an array strarr of strings and an integer k.
    Your task is to return the first longest string consisting of k consecutive strings taken in the array.
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
    :param strarr:
    :param k:
    :return:
    """
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    len_sub_str = n - k + 1
    longest_sub_str = ''
    for i in range(0, len_sub_str):
        sub_str = ''
        for j in range(0, k):
            sub_str += strarr[i+j]
        if len(sub_str)>len(longest_sub_str):
            longest_sub_str = sub_str
    return longest_sub_str


if __name__ == '__main__':
    print(solution(15))
    print(dig_pow(89, 1))
    print(diamond(-1))
    print(unique_in_order('AABBCCCCCCDEEf'))
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
