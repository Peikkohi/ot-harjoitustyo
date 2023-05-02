import tkinter as tk

from animator import Animation


class AnimationControl:
    def __init__(self, manager):
        self.manager = manager
        self.animation = Animation()
        self.run = False
        self.time = 0

    def move(self, time):
        position, ended = self.animation.frame(time)
        self.manager.position(position)
        return ended

    def animate(self):
        self.time += 0.01
        ended = self.move(self.time)
        if ended:
            self.time = 0
            self.run = False
        elif self.run:
            self.manager.schedule(self.animate)

    def play(self):
        self.run = not self.run
        if self.run:
            self.animate()

    def show(self, time):
        self.run = False
        self.move(time)

    def new(self):
        position, tween = self.animation.new()
        if tween is not None:
            self.manager.tween(self, tween)
        self.manager.frame(self, position)

    def uniform_show(self, time):
        self.show(time / 100 * self.animation.max_time())
