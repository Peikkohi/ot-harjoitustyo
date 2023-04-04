import unittest

from animator import AnimationHandler, Animator

class AnimationHandler_test(unittest.TestCase):
    def setUp(self):
        animator = Animator((0, 0))
        animator.add_frame((0, 0))
        self.handler = AnimationHandler(animator, lambda x, y: None, None)
        self.failing_branch = True

    def remove_failing(self):
        self.failing_branch = False

    def test_init(self):
        self.assertEqual(self.handler.play, False)

    def test_toggle(self):
        self.handler.update = self.remove_failing
        self.handler.toggle()
        self.assertFalse(self.failing_branch)

    def test_double_toggle(self):
        self.handler.play = True
        self.handler.update = self.fail
        self.handler.toggle()

    def test_update(self):
        self.handler.after = lambda a, b: self.fail()
        self.handler.update()

    def test_update_play(self):
        self.handler.after = lambda a, b: self.remove_failing()
        self.handler.toggle()
        self.assertFalse(self.failing_branch)
