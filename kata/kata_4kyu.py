# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


def hamming(n):
    # TODO: need optimize
    """
    The first smallest Hamming number is 1 = 203050
    The second smallest Hamming number is 2 = 213050
    The third smallest Hamming number is 3 = 203150
    The fourth smallest Hamming number is 4 = 223050
    The fifth smallest Hamming number is 5 = 203051
    :param n:
    :return:
    """
    hamming_list = []
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                hamming_list.append(2 ** i * 3 ** j * 5 ** k)
    for i in range(0, n ** 3):
        for j in range(i, n ** 3):
            if hamming_list[i] > hamming_list[j]:
                temp = hamming_list[i]
                hamming_list[i] = hamming_list[j]
                hamming_list[j] = temp
    return hamming_list[n - 1]


def valid_sudoku_solution(board):
    """
    Sudoku Solution Validator
    输入矩阵，检查是否满足数独条件
    :param board:
    :return:
    """
    unit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):
        temp_list = []
        for j in range(0, 9):
            temp_list.append(board[j][i])
        if sorted(temp_list) != unit:
            return False
        elif sorted(board[i]) != unit:
            return False
    matrix_pointer = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    for pointer in matrix_pointer:
        temp_list = []
        for i in range(0, 3):
            for j in range(0, 3):
                temp_list.append(board[pointer[0] + i][pointer[1] + j])
        if sorted(temp_list) != unit:
            return False
    return True


def is_valid_ip(strng):
    s = strng.split('.')
    if len(s) != 4:
        return False
    for i in range(0, len(s)):
        if s[i][0] == '0':
            return False
        if s[i].isdigit() != True:
            return False
        try:
            if int(s[i]) > 255 or int(s[i]) < 1:
                return False
        except ValueError:
            return False
    return True


if __name__ == '__main__':
    # print(hamming(5))
    # print(valid_sudoku_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
    #                              [6, 7, 2, 1, 9, 5, 3, 4, 8],
    #                              [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #                              [8, 5, 9, 7, 6, 1, 4, 2, 3],
    #                              [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #                              [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #                              [9, 6, 1, 5, 3, 7, 2, 8, 4],
    #                              [2, 8, 7, 4, 1, 9, 6, 3, 5],
    #                              [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
    print(is_valid_ip('111.222.21 .111'))
