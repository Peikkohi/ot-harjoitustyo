import unittest

from animator import Animation

class TestAnimation(unittest.TestCase):
    def setUp(self):
        self.animation = Animation()
    
    def test_new(self):
        position, tween = self.animation.new()
        self.assertEqual(position.index, 0)
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)
        self.assertIsNone(tween)
        self.assertEqual(self.animation.max_time(), 0)
        position, tween = self.animation.new()
        self.assertEqual(position.index, 1)
        self.assertEqual(tween.index, 0)
        self.assertEqual(tween.current, 'lerp')
        self.assertEqual(self.animation.max_time(), 1)

    def test_frame(self):
        self.animation.new()
        position, tween = self.animation.new()
        position.x = 500
        position.y = 300
        frame, success = self.animation.frame(0.5)
        frame_x, frame_y = frame
        self.assertAlmostEqual(frame_x, 250)
        self.assertAlmostEqual(frame_y, 150)
        self.assertTrue(success)

    def test_frame_max_time(self):
        position, _ = self.animation.new()
        frame, success = self.animation.frame(0)
        frame_x, frame_y = frame
        self.assertEqual(frame_x, position.x)
        self.assertEqual(frame_y, position.y)
        self.assertFalse(success)
