
def lerp(n, m, t):
    return n * (1 - t) + m * t

class Animator():
    def __init__(self, pos):
        self.frames = [pos]
        self.tweens = []
        self.time = 0

    def add_frame(self, frame, tween=lerp):
        self.frames.append(frame)
        self.tweens.append(tween)

    def animate(self):
        self.time += 0.05
        self.time %= len(self.tweens)
        i = int(self.time)
        x1, y1 = self.frames[i]
        x2, y2 = self.frames[i + 1]
        return self.tweens[i](x1, x2, self.time - i), \
                self.tweens[i](y1, y2, self.time - i)

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
        x, y = self.animator.animate()
        self.moveto(x, y)
        if self.play:
            self.after(10, self.update)
