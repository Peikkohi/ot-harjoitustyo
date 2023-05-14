class Keyframe:
    """Container for keyframe data.

    Attributes:
        timestamp: time for when keyframe is used.
        x: Horizontal position of an animated object
        y: Vertical position.
    """
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.x = 0
        self.y = 0

class Inbetween:
    """Container for transitions between keyframe data.

    Attributes:
        timestamp: time for the start of the transition.
        current: value of the selected option.
    """
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.current = 'lerp'

    def __call__(self, start, end, phase):
        return dict(zip(self.options, self.inbetweens)) \
                [self.current](start, end, phase)

    @staticmethod
    def lerp(start, end, phase):
        return start * (1 - phase) + end * phase

    @staticmethod
    def ease_in(start, end, phase):
        return Inbetween.lerp(start, end, phase * phase * phase)

    @staticmethod
    def ease_out(start, end, phase):
        inverse = 1 - phase
        return Inbetween.lerp(start, end, 1 - inverse * inverse * inverse)

    options = ('lerp', 'ease in', 'ease out')
    inbetweens = (lerp, ease_in, ease_out)



class Animation:
    """Class for calculating the position data for given time.

    Animation uses list of keyframes and the transitions between them to
    calculate positions for given time. The method "create_keyframe"
    should be called before calling other methods. Time needs to be
    between 0 and "max_time", otherwise returns last keyframe.
    """
    def __init__(self):
        self.__keyframes = []
        self.__inbetweens = []

    def max_time(self):
        """Returns length of the animation.
        """
        return len(self.__keyframes) - 1

    def create_keyframe(self):
        """Appends new keyframe and inbetween to the animation.

        Creates new instances of keyframe and inbetween, and appends them
        to the animation, returning the created keyframe and inbetween.
        For the first call of the method only keyframe is returned.

        Returns:
            the newly created keyframe
            the newly created inbetween or None
        """
        keyframe, inbetween = None, None
        if self.__keyframes:
            inbetween = Inbetween(len(self.__inbetweens))
            self.__inbetweens.append(inbetween)
        keyframe = Keyframe(len(self.__keyframes))
        self.__keyframes.append(keyframe)
        return keyframe, inbetween

    def position_of(self, time):
        """Returns a calculated position for the given time.
        
        Args:
            time: Signals which part of animation is to be returned.

        Returns:
            Horizontal, vertical positions of the animation and flag if
            animation has ended or returned early.
        """
        if time >= self.max_time() or time < 0:
            keyframe = self.__keyframes[-1]
            return keyframe.x, keyframe.y, True
        index = int(time)
        phase = time - index
        start = self.__keyframes[index]
        end = self.__keyframes[index + 1]
        transition = self.__inbetweens[index]
        return transition(start.x, end.x, phase), \
                transition(start.y, end.y, phase), False
