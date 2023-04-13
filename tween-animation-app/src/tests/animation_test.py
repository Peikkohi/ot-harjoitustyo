import unittest

from animator import animation, Pos


class TestAnimation(unittest.TestCase):
    def setUp(self):
        self.frame = animation([
            Pos(0, 0),
            Pos(10, 0),
            Pos(0, 10),
        ])

    def test_first_frame_halfway(self):
        pos = self.frame(0.5)
        self.assertAlmostEqual(pos.x, 5)
        self.assertEqual(pos.y, 0)

    def test_second_frame_halfway(self):
        pos = self.frame(1.5)
        self.assertAlmostEqual(pos.x, 5)
        self.assertAlmostEqual(pos.y, 5)
