__author__ = 'vicky.han'
import unittest
import kata


class KataTest (unittest.TestCase):
    def test_longest_consec(self):
        self.assertEquals(kata.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEquals(kata.longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEquals(kata.longest_consec([], 3), "")
        self.assertEquals(kata.longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEquals(kata.longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEquals(kata.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEquals(kata.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEquals(kata.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEquals(kata.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

# def suite():
#     katatest =KataTest()
#     suite = unittest.TestSuite()
#     suite.addTest(katatest.test_longest_consec())
#     return suite()

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # test_suite = suite()
    # runner.run(test_suite)
    unittest.main()