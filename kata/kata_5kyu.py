# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'
import math


def pig_it(text):
    """
    Simple Pig Latin
    Move the first letter of each word to the end of it, then add 'ay' to the end of the word.
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    :param text:
    :return:
    """
    word_list = text.split(" ")
    for i in range(0, len(word_list)):
        changed = ""
        for j in range(1, len(word_list[i])):
            changed += word_list[i][j]
        changed += word_list[i][0]
        if changed not in "!.?,":
            changed += 'ay'
        word_list[i] = changed
    changed_text = ' '.join(word_list)
    return changed_text


def valid_parentheses(string):
    """
    Valid Parentheses
    Write a function called validParentheses that takes a string of parentheses,
    and determines if the order of the parentheses is valid. validParentheses
    should return true if the string is valid, and false if it's invalid.
    Examples:
    validParentheses( "()" ) => returns true
    validParentheses( "(" ) => returns false
    validParentheses( "(())((()())())" ) => returns true
    :param string:
    :return:
    """
    ar_list = []
    for i in range(0, len(string)):
        if string[i] == '(':
            ar_list.append(' ')
        elif string[i] == ')':
            try:
                ar_list.pop()
            except IndexError:
                return False
    if len(ar_list) == 0:
        return True
    return False


def meters(x):
    """
    Metric Units - 1
    write a simple function that takes a number of meters, and outputs it using metric prefixes.
    In practice, meters are only measured in "mm" (thousandths of a meter), "cm" (hundredths of a meter),
    "m" (meters) and "km" (kilometers, or clicks for the US military).
    :param x:
    :return:
    """
    units_list_bigger = ['m', 'km', 'Mm', 'Gm', 'Tm', 'Pm', 'Em', 'Zm', 'Ym']
    units_list_smaller = ['m', 'dm', 'cm', 'mm', 'Dmm', 'Cmm', 'um', 'zm']

    unit_count = 0
    if x >= 1:
        while x / (10 ** 3) >= 1:
            x /= float(10 ** 3)
            unit_count += 1
        return str(int(x)) + units_list_bigger[unit_count] if x % 1 == 0 else str(x) + units_list_bigger[unit_count]
    elif 0 < x < 1:
        while True:
            x *= 10
            unit_count += 1
            if x >= 1:
                break
        return str(int(x)) + units_list_smaller[unit_count] if x % 1 == 0 else str(x) + units_list_smaller[unit_count]
    else:
        return

    # TODO: FIX IT
    # def isSolved(board):
    """
    Tic-Tac-Toe Checker
    :return:
    """


    # count_X = 0
    # count_O = 0
    # for i in range(0, 3):
    #     for j in range(0, 3):
    #         if board[i][j] == 1:
    #             count_X += 1
    #         elif board[i][j] == 2:
    #             count_O += 1
    #         elif board[i][j] == 0:
    #             pass
    #         else:
    #             return 0
    # if count_X != count_O and count_O-count_X != 1 and count_X -count_O != 1:
    #     return 0
    #
    # for i in range(0, 3):
    #     if board[i][0] == board[i][1] == board[i][2] == 1 or board[i][0] == board[i][1] == board[i][2] == 2:
    #         return int(board[i][0])
    # for i in range(0,3):
    #     if board[0][i] == board[1][i] == board[2][i] == 1 or board[0][i] == board[1][i] == board[2][i] == 2:
    #         return int(board[0][i])
    # if board[0][0] == board[1][1] == board[2][2] == 1 or board[0][2] == board[1][1] == board[2][0] == 1:
    #     return 1
    # if board[0][0] == board[1][1] == board[2][2] == 2 or board[0][2] == board[1][1] == board[2][0] == 2:
    #     return 2
    # return -1


def anagrams(word, words):
    """
    Where my anagrams at?
    返回指定单词的变形词（只有字母排列顺序不同的单词）
    :param word:指定的单词
    :param words:
    :return:
    """
    # word = "".join((lambda x: (x.sort(), x)[1])(list(word)))
    word = "".join(sorted(word))
    pointer = 0
    while pointer < len(words):
        if word != "".join(sorted(words[pointer])):
            words.pop(pointer)
        else:
            pointer += 1
    return words


class Vector:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        str1 = '(' + str(self.list[0])
        for i in range(1, self.len()):
            str1 += ',' + str(self.list[i])
        str1 += ')'
        return str1

    def len(self):
        return len(self.list)

    def equals(self, vector):
        if self.len() == vector.len():
            for i in range(0, vector.len()):
                if self.list[i] != vector.list[i]:
                    return False
            return True
        else:
            return False

    def add(self, vector):
        if self.len() == vector.len():
            result = Vector([])
            for i in range(0, vector.len()):
                result.list.append(self.list[i] + vector.list[i])
            return result
        else:
            raise IndexError

    def subtract(self, vector):
        if self.len() == vector.len():
            result = Vector([])
            for i in range(0, vector.len()):
                result.list.append(self.list[i] - vector.list[i])
            return result
        else:
            raise IndexError

    def dot(self, vector):
        result = 0
        if self.len() == vector.len():
            for i in range(0, vector.len()):
                result += self.list[i] * vector.list[i]
            return result
        else:
            raise IndexError

    def norm(self):
        result = 0
        for i in range(0, len(self.list)):
            result += self.list[i] ** 2
        return math.sqrt(result)


if __name__ == '__main__':
    # print(pig_it('Pig latin is cool'))
    # print(valid_parentheses("((awefa())f()ae)"))
    # print(meters(123456))
    # print(anagrams('abba',['aabb', 'abcd', 'bbaa', 'dada','a']))
    print(Vector([1, 2, 3]).subtract(Vector([3, 4, 5])).__str__())

