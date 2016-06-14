import unittest
import kata_5kyu
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

# if __name__ == '__main__':
#     # unittest.main()
