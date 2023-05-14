import tkinter as tk

from animation import Keyframe, Inbetween

class SettingFactory:
    """A class which combines app logic with UI elements.
    """
    def __init__(self, widget):
        self.__widget = widget

    def change_shown(self, widget):
        for children in self.__widget.slaves():
            children.pack_forget()
        widget.pack()

    def for_keyframe(self, keyframe: Keyframe):
        frame = tk.LabelFrame(self.__widget,
                text=f'Frame { keyframe.timestamp }')
        def scale(to):
            scale = tk.Scale(frame, to=to, orient='horizontal')
            scale.pack()
            def wrapper(f):
                scale['command'] = f
            return wrapper
        @scale(to=800)
        def set_x(value):
            keyframe.x = int(value)
        @scale(to=600)
        def set_y(value):
            keyframe.y = int(value)
        return frame

    def for_inbetween(self, inbetween: Inbetween):
        frame = tk.LabelFrame(self.__widget,
                text=f'Tween { inbetween.timestamp }')
        def change_to(option):
            inbetween.current = option
        optionmenu = tk.OptionMenu(frame, tk.Variable(),
                *inbetween.options, command=change_to)
        optionmenu.pack(expand=True, fill='x')
        return frame

