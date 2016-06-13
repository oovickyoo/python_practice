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


def my_parse_int(strings):
    """
    String to integer conversion
    You are asked to write a myParseInt method with the following rules:
    It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
    For all other strings (including the ones representing float values), it should return NaN
    It should assume that all numbers are not signed and written in base 10
    :param strings:
    :return:
    """
    strings = strings.strip()
    num_list = '0123456789'
    for i in range(0, len(strings)):
        count = 0
        for j in range(0, len(num_list)):
            if strings[i] == num_list[j]:
                break
            else:
                count += 1
        if count == 10:
            return 'NaN'
    return int(strings)


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

if __name__ == '__main__':
    # print(my_parse_int(" 12"))
    print(diamond(-1))
    # s=diamond(3)

