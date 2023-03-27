import unittest
import random

import random


def truth(s):
    b = s.lower()
    return b


def test_in():
    colors = ['khaki', 'black', 'white', 'brown', 'pink']
    return random.choice(colors)


def greater(a, b):
    c = a + b
    return c


def less():
    words = ['cat', 'home', 'cat', 'mom', 'dad', 'I', 'you', 'road', 'mime', 'pig']
    return random.choice(words)


def equal():
    skate = {'Ilya Malinin', 'Kevin Aymoz', 'Shoma Uno', 'Junhwan Cha'}
    return skate

class MyTestCase(unittest.TestCase):
    def test_truth(self):
        s = 'SNDGFNRTJ'
        b = truth(s)
        self.assertTrue(b.islower())
        self.assertFalse(s.islower())

    def test_in_notin(self):
        rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'violet']
        colors = rainbow
        color_1 = random.choice(colors)
        color_2 = test_in()
        self.assertIn(color_1, rainbow)
        self.assertNotIn(color_2, rainbow)

    def test_greater(self):
        a = 20
        b = 60
        c = greater(a,b)
        self.assertGreater(c, a)

    def test_less(self):
        length = 4
        word = less()
        self.assertLess(len(word), length)

    def test_countequal(self):
        skaters = ['Shoma Uno', 'Junhwan Cha', 'Ilya Malinin', 'Kevin Aymoz']
        skaters1 = equal()
        self.assertCountEqual(skaters, skaters1)


if __name__ == '__main__':
    unittest.main()
