from animation import Animation

class AnimationPlayer:
    """Class responsible for keeping track of time and if animation is
    running.
    """
    def __init__(self, animation: Animation):
        self.__animation = animation
        self.__run = False
        self.__time = 0

    def switch_to(self, time: float, normalized=False):
        """Switches animation to given time and returns position of it.

        Arguments:
            time: timestamp of the phase to be switched to.
            normalized: flag for when time is percent of the whole
                animation length.

        Returns:
            Horizontal and vertical position of the given time.
        """
        if normalized:
            time = time / 100 * self.__animation.max_time()
        self.__run = False
        self.__time = time
        pos_x, pos_y, _ = self.__animation.position_of(time)
        return pos_x, pos_y

    def next_position(self):
        """Proceeds with the animation returning the next positions.

        Returns:
            Horizontal and vertical position of animation, and state of
            if animation is still running.
        """
        self.__time += 0.01
        pos_x, pos_y, ended = self.__animation.position_of(self.__time)
        if ended:
            self.__run = False
            self.__time = 0
        return pos_x, pos_y, self.__run

    def toggle(self):
        """Turns animation on/off returning if animation is running.
        """
        self.__run = not self.__run
        return self.__run
