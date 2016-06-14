# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


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


if __name__ == '__main__':
    print(my_parse_int(" 12"))




