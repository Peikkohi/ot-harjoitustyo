import unittest

from animator import scheduled


class TestScheduled(unittest.TestCase):
    def after(self, interval, callback):
        self.interval = interval
        callback()

    def test_scheduled_called(self):
        self.fail = True

        @scheduled(self, 1)
        def wrap():
            self.fail = False

        wrap()

        if self.fail:
            self.fail()

    def test_scheduled_wrapping(self):
        @scheduled(self, 1)
        def wrap():
            self.assertNotEqual(wrap, None)
        wrap()

    def test_scheduled_args_passing(self):
        @scheduled(self, 1)
        def wrap(arg):
            self.assertEqual(arg, 1)

        wrap(1)

    def test_scheduled_interval(self):
        @scheduled(self, 1)
        def wrap():
            pass
        wrap()
        self.assertEqual(self.interval, 1)
