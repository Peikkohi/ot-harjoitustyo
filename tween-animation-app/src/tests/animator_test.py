import unittest

from animator import Animator


class DummyManager:
    def __init__(self):
        self.args = dict()

        self.schedule = self.create_method('schedule')
        self.position = self.create_method('position')
        self.setting = self.create_method('setting')

    def create_method(self, name):
        self.args[name] = []

        def method(*args):
            self.args[name].append(args)
        return method


class TestAnimator(unittest.TestCase):
    def setUp(self):
        self.manager = DummyManager()
        self.animator = Animator(self.manager)

    def test_init(self):
        self.assertIs(self.animator.manager, self.manager)
        self.assertEqual(self.animator.frames, [])
        self.assertEqual(self.animator.tweens, [])
        self.assertFalse(self.animator.run)
        self.assertEqual(self.animator.time, 0)

    def test_new_ones(self):
        self.animator.new()
        self.assertEqual(self.animator.frames, [[0, 0]])
        self.assertEqual(self.animator.tweens, [])
        setting = self.manager.args['setting']
        self.assertEqual(len(setting), 1)
        self.assertIs(setting[0][0], self.animator)
        self.assertEqual(setting[0][1], [[0, 0]])

    def test_new_twice(self):
        self.animator.new()
        self.animator.new()
        self.assertEqual(self.animator.tweens[0].__name__, 'lerp')
        setting = self.manager.args['setting']
        self.assertEqual(len(setting), 3)
        self.assertIs(setting[1][1], self.animator.tweens)
        self.assertEqual(len(setting[1][2]), 3)

    def test_show(self):
        self.animator.new()
        self.animator.run = True
        self.animator.show(0)
        position = self.manager.args['position']
        self.assertFalse(self.animator.run)
        self.assertEqual(position[0][0], [0, 0])

    def test_play_end_of_animation(self):
        self.animator.new()
        self.animator.play()
        self.assertEqual(self.animator.time, 0)
        self.assertFalse(self.animator.run)

    def test_play_on(self):
        self.animator.run = True
        self.animator.play()
        self.assertFalse(self.animator.run)

    def test_play_off(self):
        self.animator.new()
        self.animator.new()
        self.animator.play()
        position = self.manager.args['position']
        schedule = self.manager.args['schedule']
        self.assertTrue(self.animator.run)
        # self.assertIs(schedule[0][0], self.animator.animate)
        self.assertAlmostEqual(position[0][0][0], 0)
        self.assertAlmostEqual(position[0][0][1], 0)
