# -*- coding: UTF-8 -*-
__author__ = 'vicky.han'


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
        while x/(10**3) >= 1:
            x /= float(10**3)
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


if __name__ == '__main__':
    # print(pig_it('Pig latin is cool'))
    # print(valid_parentheses("((awefa())f()ae)"))
    print(meters(123456))
