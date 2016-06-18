import unittest
import kata_5kyu
from kata_5kyu import *
__author__ = 'vicky.han'


class KataTest (unittest.TestCase):

    def test_pig_it(self):
        self.assertEquals(kata_5kyu.pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEquals(kata_5kyu.pig_it('This is my string'), 'hisTay siay ymay tringsay')
        self.assertEquals(kata_5kyu.pig_it('Oay emporatay oay oresmay !'), 'ayOay mporatayeay ayoay resmayoay !')
        self.assertEquals(kata_5kyu.pig_it('Is this ok ?'), 'sIay histay koay ?')

    def test_valid_parentheses(self):
        self.assertEquals(kata_5kyu.valid_parentheses(")"), False)
        self.assertEquals(kata_5kyu.valid_parentheses("("), False)
        self.assertEquals(kata_5kyu.valid_parentheses(""), True)
        self.assertEquals(kata_5kyu.valid_parentheses("hi)("), False)
        self.assertEquals(kata_5kyu.valid_parentheses("hi(hi)"), True)
        self.assertEquals(kata_5kyu.valid_parentheses("("), False)
        self.assertEquals(kata_5kyu.valid_parentheses("hi(hi)("), False)
        self.assertEquals(kata_5kyu.valid_parentheses("((())()())"), True)
        self.assertEquals(kata_5kyu.valid_parentheses("(c(b(a)))(d)"), True)
        self.assertEquals(kata_5kyu.valid_parentheses("hi(hi))("), False)

    def test_meters(self):
        self.assertEquals(kata_5kyu.meters(1), "1m")
        self.assertEquals(kata_5kyu.meters(999), "999m")
        self.assertEquals(kata_5kyu.meters(123456), "123.456km")
        self.assertEquals(kata_5kyu.meters(12300000), "12.3Mm")
        self.assertEquals(kata_5kyu.meters(9e9), "9Gm")
        self.assertEquals(kata_5kyu.meters(9e12), "9Tm")
        self.assertEquals(kata_5kyu.meters(9e15), "9Pm")
        self.assertEquals(kata_5kyu.meters(9e18), "9Em")
        self.assertEquals(kata_5kyu.meters(9e21), "9Zm")
        self.assertEquals(kata_5kyu.meters(9e24), "9Ym")

    def test_isSolved(self):
        # TODO:
        pass

    def test_anagrams(self):
        self.assertEquals(kata_5kyu.anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEquals(kata_5kyu.anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
        self.assertEquals(kata_5kyu.anagrams('a', ['a', 'b', 'c', 'd']), ['a'])
        self.assertEquals(kata_5kyu.anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']), ['ab', 'ba'])
        self.assertEquals(kata_5kyu.anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']), ['aabb', 'bbaa', 'abab', 'baba', 'baab'])
        self.assertEquals(kata_5kyu.anagrams('big', ['gig', 'dib', 'bid', 'biig']), [])

    def test_class_vector(self):
        a = Vector([1, 2, 3])
        b = Vector([3, 4, 5])
        c = Vector([5, 6, 7, 8])
        self.assertEquals(a.add(b).equals(Vector([4, 6, 8])), 1)
        self.assertEquals(a.subtract(b).equals(Vector([-2, -2, -2])), 1)
        self.assertEquals(a.dot(b), 26)
        self.assertEquals(b.dot(a), a.dot(b))
        self.assertEquals(a.norm() - math.sqrt(14) < 0.1, 1)
        self.assertEquals(b.norm() - math.sqrt(50) < 0.1, 1)
        self.assertEquals(c.norm() - math.sqrt(174) < 0.1, 1)
        self.assertEquals(a.equals(Vector([1, 2, 3])), 1)
        self.assertEquals(b.equals(Vector([3, 4, 5])), 1)
        self.assertNotEqual(a.equals(b), 1)
        self.assertNotEqual(b.equals(c), 1)
        self.assertNotEqual(a.equals(c), 1)
        self.assertEquals(str(a), "(1,2,3)")
        self.assertEquals(str(b), "(3,4,5)")
        self.assertEquals(str(c), "(5,6,7,8)")


# if __name__ == '__main__':
#     # unittest.main()
