from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])


def mix(start: float, end: float, time: float):
    return start * (1 - time) + end * time


class Animator():
    def __init__(self, pos: Pos):
        self.frames = [pos]
        self.tweens = []
        self.time = 0

    def add_frame(self, frame: Pos, tween=mix):
        self.frames.append(frame)
        self.tweens.append(tween)

    def animate(self):
        self.time += 0.05
        self.time %= len(self.tweens)
        index = int(self.time)
        start = self.frames[index]
        end = self.frames[index + 1]
        tween = self.tweens[index]
        time = self.time - index
        return Pos(
            x=tween(start.x, end.x, time),
            y=tween(start.y, end.y, time),
        )


class AnimationHandler():
    def __init__(self, animator, moveto, after):
        self.play = False
        self.animator = animator
        self.moveto = moveto
        self.after = after

    def toggle(self):
        self.play = not self.play
        if self.play:
            self.update()

    def update(self):
        pos = self.animator.animate()
        self.moveto(pos.x, pos.y)
        if self.play:
            self.after(10, self.update)
