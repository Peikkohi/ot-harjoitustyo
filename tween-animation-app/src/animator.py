
def lerp(start, end, phase):
    return start * (1 - phase) + end * phase


def ease_in(start, end, phase):
    return lerp(start, end, phase * phase * phase)


def ease_out(start, end, phase):
    inverse = 1 - phase
    return lerp(start, end, 1 - inverse * inverse * inverse)


class Animator:
    def __init__(self, manager):
        self.manager = manager
        self.frames = []
        self.tweens = []
        self.run = False
        self.time = 0

    def max_time(self):
        return len(self.frames) - 1

    def frame(self, time):
        if time >= self.max_time():
            self.manager.position(self.frames[-1])
            return False
        index = int(time)
        phase = time - index
        start_x, start_y = self.frames[index]
        end_x, end_y = self.frames[index + 1]
        tween = self.tweens[index]
        self.manager.position(
            (tween(start_x, end_x, phase), tween(start_y, end_y, phase)))
        return True

    def animate(self):
        self.time += 0.01
        success = self.frame(self.time)
        if not success:
            self.time = 0
            self.run = False

        if self.run:
            self.manager.schedule(self.animate)

    def play(self):
        self.run = not self.run
        if self.run:
            self.animate()

    def show(self, time):
        self.run = False
        self.frame(time)

    def new(self):
        if len(self.frames) > 0:
            self.tweens.append(lerp)

            self.manager.setting(self, self.tweens,
                                 [lerp, ease_in, ease_out])

        self.frames.append([0, 0])

        self.manager.setting(self, self.frames)
