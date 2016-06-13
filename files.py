# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'

import os


def read_files():
    """
    读取文件
    """
    f = open('./text', 'r').read()
    print(f)


def read_by_line():
    """
    逐行读取文件
    """
    f = open('./text', 'r')
    for line in f.readlines():
        print(line)

if __name__ == '__main__':
    read_files()
