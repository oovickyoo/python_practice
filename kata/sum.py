# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


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
    k = x % n
    if k == 0:
        return x/n
    else:
        return -1

if __name__ == '__main__':
    print(dig_pow(89, 1))