# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(str(i)+"*"+str(j)+"="+str(i*j)+";"),
        print('\n'),


def flower():
    """
    打印出所有的“水仙花数”
    所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

    :return:
    """
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i*100+j*10+k == i**3+j**3+k**3:
                    print(i*100+j*10+k)


if __name__ == "__main__":
    flower()
