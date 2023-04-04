import unittest
from animator import Animator

class TestAnimator(unittest.TestCase):
    def setUp(self):
        self.animator = Animator((0, 0))

    def test_init(self):
        self.assertEqual(self.animator.frames[0], (0, 0))

    def test_add_frame_counts(self):
        self.animator.add_frame((10, 0))
        self.assertEqual(len(self.animator.frames), 2)
        self.assertEqual(len(self.animator.tweens), 1)

    def test_add_frame_defaults(self):
        self.animator.add_frame((10, 0))
        self.assertEqual(self.animator.tweens[0](0, 10, 0.5), 5)

    def test_add_frame_tween(self):
        f = lambda n, m, t: m 
        self.animator.add_frame((10, 0), f)
        self.assertEqual(self.animator.tweens[0](0, 10, 0), 10)

    def test_animate_first_frame(self):
        self.animator.add_frame((10, 0))
        pos = None
        for _ in range(10):
            pos = self.animator.animate()
        x, y = pos
        self.assertAlmostEqual(x, 5)

    def test_animate_second_frame(self):
        self.animator.add_frame((10, 0))
        self.animator.add_frame((10, 10))
        pos = None
        for _ in range(30):
            pos = self.animator.animate()
        x, y = pos
        self.assertAlmostEqual(x, 10)
        self.assertAlmostEqual(y, 5)
