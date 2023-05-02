import unittest

from animator import Tween


class TestTweens(unittest.TestCase):
    def setUp(self):
        self.tween = Tween(0)

    def test_lerp(self):
        self.tween.set_current('lerp')
        n = 0
        while n < 1:
            self.assertAlmostEqual(self.tween(0, 1, n), n)
            n += 0.1

    def test_ease_in(self):
        self.tween.set_current('ease in')
        n = 0
        while n < 1:
            self.assertAlmostEqual(self.tween(0, 1, n), n * n * n)
            n += 0.1

    def test_ease_out(self):
        self.tween.set_current('ease out')
        n = 0
        while n < 1:
            inverse = 1 - n
            self.assertAlmostEqual(
                self.tween(0, 1, n), 1 - inverse * inverse * inverse)
            n += 0.1
