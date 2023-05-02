
class Position:
    def __init__(self, index):
        self.index = index
        self.horizontal_position = 0
        self.vertical_position = 0

    def set_x(self, value):
        self.horizontal_position = value

    def set_y(self, value):
        self.vertical_position = value

    def __iter__(self):
        return iter((self.horizontal_position, self.vertical_position))


class Tween:
    @staticmethod
    def lerp(start, end, phase):
        return start * (1 - phase) + end * phase

    @staticmethod
    def ease_in(start, end, phase):
        return Tween.lerp(start, end, phase * phase * phase)

    @staticmethod
    def ease_out(start, end, phase):
        inverse = 1 - phase
        return Tween.lerp(start, end, 1 - inverse * inverse * inverse)

    options = ('lerp', 'ease in', 'ease out')
    tweens = (lerp, ease_in, ease_out)

    def __init__(self, index):
        self.index = index
        self.current = 'lerp'

    def set_current(self, value):
        assert value in self.options
        self.current = value

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
            return self.frames[-1], True
        index = int(time)
        phase = time - index
        start_x, start_y = self.frames[index]
        end_x, end_y = self.frames[index + 1]
        tween = self.tweens[index]
        return (tween(start_x, end_x, phase), tween(start_y, end_y, phase)), False

    def new(self):
        position, tween = None, None
        if self.frames:
            tween = Tween(len(self.tweens))
            self.tweens.append(tween)
        position = Position(len(self.frames))
        self.frames.append(position)
        return position, tween
