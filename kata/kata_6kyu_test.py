import unittest
import kata_6kyu
__author__ = 'vicky.han'


class KataTest (unittest.TestCase):

    def test_longest_consec(self):
        self.assertEquals(kata_6kyu.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEquals(kata_6kyu.longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEquals(kata_6kyu.longest_consec([], 3), "")
        self.assertEquals(kata_6kyu.longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEquals(kata_6kyu.longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEquals(kata_6kyu.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEquals(kata_6kyu.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEquals(kata_6kyu.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEquals(kata_6kyu.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")


# if __name__ == '__main__':
#     # unittest.main()
