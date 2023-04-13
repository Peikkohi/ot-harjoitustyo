from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])


def scheduled(scheduler, interval):
    def wrapper(call):
        def wrap(*args, **kwargs):
            scheduler.after(interval, lambda: call(*args, **kwargs))
        return wrap
    return wrapper


def animation(frames):
    def frame(time):
        index = int(time)
        phase = time - index
        start, end = frames[index], frames[index + 1]

        def lerp(start, end):
            return start * (1 - phase) + end * phase
        return Pos(x=lerp(start.x, end.x), y=lerp(start.y, end.y))
    return frame


def drawable(canvas, *args, **kwargs):
    obj = canvas.create_rectangle(*args, **kwargs)

    def move_to(pos):
        canvas.moveto(obj, pos.x, pos.y)
    return move_to
