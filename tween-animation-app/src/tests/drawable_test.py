import unittest

from animator import drawable, Pos


class TestDrawable(unittest.TestCase):
    def create_rectangle(self, value):
        return value

    def moveto(self, value, pos_x, pos_y):
        self.value = value
        self.pos = Pos(pos_x, pos_y)

    def setUp(self):
        self.move_to = drawable(self, 1)

    def test_value_passing(self):
        self.move_to(Pos(0, 0))
        self.assertEqual(self.value, 1)
        self.assertEqual(self.pos, Pos(0, 0))
