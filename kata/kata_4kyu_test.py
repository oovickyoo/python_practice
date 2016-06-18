import unittest
import kata_4kyu

__author__ = 'vicky.han'


class KataTest(unittest.TestCase):
    def test_valid_sudoku_solution(self):
        self.assertEquals(kata_4kyu.valid_sudoku_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                                           [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                                           [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                                           [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                                           [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                                           [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                                           [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                                           [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                                           [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True)
        self.assertEquals(kata_4kyu.valid_sudoku_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                                           [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                                           [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                                           [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                                           [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                                           [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                                           [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                                           [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                                           [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False)
        self.assertEquals(kata_4kyu.valid_sudoku_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                                                           [4, 9, 8, 2, 6, 1, 3, 7, 5],
                                                           [7, 5, 6, 3, 8, 4, 2, 1, 9],
                                                           [6, 4, 3, 1, 5, 8, 7, 9, 2],
                                                           [5, 2, 1, 7, 9, 3, 8, 4, 6],
                                                           [9, 8, 7, 4, 2, 6, 5, 3, 1],
                                                           [2, 1, 4, 9, 3, 5, 6, 8, 7],
                                                           [3, 6, 5, 8, 1, 7, 9, 2, 4],
                                                           [8, 7, 9, 6, 4, 2, 1, 5, 3]]), True)
        self.assertEquals(kata_4kyu.valid_sudoku_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                                                           [4, 9, 8, 2, 6, 1, 3, 7, 5],
                                                           [7, 5, 6, 3, 8, 4, 2, 1, 9],
                                                           [6, 4, 3, 1, 5, 8, 7, 9, 2],
                                                           [5, 2, 1, 7, 9, 3, 8, 4, 6],
                                                           [9, 8, 7, 4, 2, 6, 5, 3, 1],
                                                           [2, 1, 4, 9, 3, 5, 6, 8, 7],
                                                           [3, 6, 5, 8, 1, 7, 9, 2, 4],
                                                           [8, 7, 9, 6, 4, 2, 1, 3, 5]]), False)
        self.assertEquals(kata_4kyu.valid_sudoku_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                                                           [4, 9, 8, 2, 6, 0, 3, 7, 5],
                                                           [7, 0, 6, 3, 8, 0, 2, 1, 9],
                                                           [6, 4, 3, 1, 5, 0, 7, 9, 2],
                                                           [5, 2, 1, 7, 9, 0, 8, 4, 6],
                                                           [9, 8, 0, 4, 2, 6, 5, 3, 1],
                                                           [2, 1, 4, 9, 3, 5, 6, 8, 7],
                                                           [3, 6, 0, 8, 1, 7, 9, 2, 4],
                                                           [8, 7, 0, 6, 4, 2, 1, 3, 5]]), False)
        self.assertEquals(kata_4kyu.valid_sudoku_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                           [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                                           [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                                           [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                                           [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                                           [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                                           [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                                           [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                                           [9, 1, 2, 3, 4, 5, 6, 7, 8]]), False)

    def test_is_valid_ip(self):
        self.assertEquals(kata_4kyu.is_valid_ip('12.255.56.1'),     True)
        self.assertEquals(kata_4kyu.is_valid_ip(''),                False)
        self.assertEquals(kata_4kyu.is_valid_ip('abc.def.ghi.jkl'), False)
        self.assertEquals(kata_4kyu.is_valid_ip('123.456.789.0'),   False)
        self.assertEquals(kata_4kyu.is_valid_ip('12.34.56'),        False)
        self.assertEquals(kata_4kyu.is_valid_ip('12.34.56 .1'),     False)
        self.assertEquals(kata_4kyu.is_valid_ip('12.34.56.-1'),     False)
        self.assertEquals(kata_4kyu.is_valid_ip('123.045.067.089'), False)
# if __name__ == '__main__':
#     # unittest.main()
