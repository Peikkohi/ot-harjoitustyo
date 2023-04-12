import unittest
from animator import Animator, Pos


class TestAnimator(unittest.TestCase):
    def setUp(self):
        self.animator = Animator(Pos(x=0, y=0))

    def test_init(self):
        self.assertEqual(self.animator.frames[0], Pos(x=0, y=0))

    def test_add_frame_counts(self):
        self.animator.add_frame(Pos(x=10, y=0))
        self.assertEqual(len(self.animator.frames), 2)
        self.assertEqual(len(self.animator.tweens), 1)

    def test_add_frame_defaults(self):
        self.animator.add_frame(Pos(x=10, y=0))
        self.assertEqual(self.animator.tweens[0](0, 10, 0.5), 5)

    def test_add_frame_tween(self):
        self.animator.add_frame(Pos(x=10, y=0), lambda n, m, t: m)
        self.assertEqual(self.animator.tweens[0](0, 10, 0), 10)

    def test_animate_first_frame(self):
        self.animator.add_frame(Pos(x=10, y=0))
        pos = None
        for _ in range(10):
            pos = self.animator.animate()
        self.assertAlmostEqual(pos.x, 5)

    def test_animate_second_frame(self):
        self.animator.add_frame(Pos(x=10, y=0))
        self.animator.add_frame(Pos(x=10, y=10))
        pos = None
        for _ in range(30):
            pos = self.animator.animate()
        self.assertAlmostEqual(pos.x, 10)
        self.assertAlmostEqual(pos.y, 5)
