# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


def multiplication_table():
    """
    打印九九乘法表
    tips：
    print语句后加逗号，不自动换行
    循环，for i in range(start, stop, step)
    """
    for i in range(1, 10):
        for j in range(1, i+1):
            print(str(i)+"*"+str(j)+"="+str(i*j)+";"),
        print('\n'),

if __name__ == "__main__":
    multiplication_table()
