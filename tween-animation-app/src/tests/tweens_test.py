import unittest

from animator import lerp, ease_in, ease_out

class TestTweens(unittest.TestCase):
    def test_lerp(self):
        n = 0
        while n < 1:
            self.assertAlmostEqual(lerp(0, 1, n), n)
            n += 0.1

    def test_ease_in(self):
        n = 0
        while n < 1:
            self.assertAlmostEqual(ease_in(0, 1, n), n * n * n)
            n += 0.1

    def test_ease_out(self):
        n = 0
        while n < 1:
            inverse = 1 - n
            self.assertAlmostEqual(ease_out(0, 1, n), 1 - inverse * inverse * inverse)
            n += 0.1
