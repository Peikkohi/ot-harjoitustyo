
class Position:
    def __init__(self, index):
        self.index = index
        self.x = 0
        self.y = 0

    def __iter__(self):
        return iter((self.x, self.y))

def lerp(start, end, phase):
    return start * (1 - phase) + end * phase


def ease_in(start, end, phase):
    return lerp(start, end, phase * phase * phase)


def ease_out(start, end, phase):
    inverse = 1 - phase
    return lerp(start, end, 1 - inverse * inverse * inverse)

class Tween:
    options = ('lerp', 'ease in', 'ease out')
    tweens = (lerp, ease_in, ease_out)

    def __init__(self, index):
        self.index = index
        self.current = 'lerp'

    def __call__(self, start, end, phase):
        return dict(zip(self.options,
            self.tweens))[self.current](start, end, phase)

class Animation:
    def __init__(self):
        self.frames = []
        self.tweens = []

    def max_time(self):
        return len(self.frames) - 1

    def frame(self, time):
        if time >= self.max_time():
            return self.frames[-1], False
        index = int(time)
        phase = time - index
        start_x, start_y = self.frames[index]
        end_x, end_y = self.frames[index + 1]
        tween = self.tweens[index]
        return (tween(start_x, end_x, phase), tween(start_y, end_y, phase)), True

    def new(self):
        position, tween = None, None
        if self.frames != []:
            tween = Tween(len(self.tweens))
            self.tweens.append(tween)
        position = Position(len(self.frames))
        self.frames.append(position)
        return position, tween

class Animator(Animation):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.run = False
        self.time = 0

    def animate(self):
        self.time += 0.01
        position, success = self.frame(self.time)
        self.manager.position(position)
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
        position, _ = self.frame(time)
        self.manager.position(position)

    def new(self):
        position, tween = super().new()
        if tween != None:
            self.manager.setting(self, tween, is_tween=True)
        self.manager.setting(self, position)
