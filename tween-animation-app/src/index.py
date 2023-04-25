import tkinter as tk

from animator import Animator


class Setting:
    def __init__(self, lst, settings, timeline, animation):
        self.animation = animation
        self.settings = settings
        self.lst = lst
        self.index = len(lst) - 1

        self.frame = tk.LabelFrame(settings)
        self.button = tk.Button(timeline, command=self.switch)
        self.button.pack(side='left')

    def switch(self):
        for widget in self.settings.slaves():
            widget.pack_forget()
        self.frame.pack()
        self.animation.show(self.index)


class FrameSetting(Setting):
    def __init__(self, lst, setting, timeline, animation):
        super().__init__(lst, setting, timeline, animation)
        self.frame.config(text=f'Frame { self.index }')
        self.button.config(text=self.index)
        self.create_scale(800, 0)
        self.create_scale(600, 1)

    def create_scale(self, max_val, elem):
        scale = tk.Scale(self.frame, to=max_val, orient='horizontal')
        scale.pack()

        @lambda f: scale.config(command=f)
        def update(val):
            self.lst[self.index][elem] = int(val)


class TweenSetting(Setting):
    def __init__(self, lst, setting, timeline, animation, options):
        super().__init__(lst, setting, timeline, animation)
        self.options = options
        self.frame.config(text=f'Tween { self.index }')
        self.button.config(text='...')

        option_menu = tk.OptionMenu(self.frame,
                                    tk.Variable(), *options, command=self.update)
        option_menu.pack()

    def update(self, val):
        self.lst[self.index] = self.options[val]


class Manager:
    def __init__(self, settings, timeline, schedule, position):
        self.settings = settings
        self.timeline = timeline
        self.schedule = schedule
        self.position = position

    def setting(self, animation, lst, options=None):
        if options:
            TweenSetting(lst, self.settings, self.timeline, animation,
                         dict((tween.__name__, tween) for tween in options))
        else:
            FrameSetting(lst, self.settings, self.timeline, animation)


if __name__ == '__main__':
    root = tk.Tk()

    render_frame = tk.Frame(root)
    render_frame.pack(side='top', fill='x')

    canvas = tk.Canvas(render_frame, width=800, height=600, bg='white')
    canvas.pack(side='left')

    drawable = canvas.create_oval(0, 0, 50, 50, fill='green')

    settings_frame = tk.Frame(render_frame)
    settings_frame.pack(side='left', fill='both')

    timeline_scale = tk.Scale(root, orient='horizontal', showvalue=False)
    timeline_scale.pack(side='top', fill='x')

    toolbar_frame = tk.Frame(root)
    toolbar_frame.pack(side='top', fill='x')

    select_frame = tk.Frame(toolbar_frame)
    select_frame.pack(side='left', fill='x', expand=True)

    timeline_frame = tk.Frame(select_frame)
    timeline_frame.pack(side='left')

    new_button = tk.Button(select_frame, text='new')
    new_button.pack(side='left')

    play_button = tk.Button(toolbar_frame, text='play')
    play_button.pack(side='right', fill='x')

    manager = Manager(
        settings_frame, timeline_frame,
        lambda update: root.after(17, update),
        lambda pos: canvas.moveto(drawable, *pos),
    )
    animator = Animator(manager)

    new_button['command'] = animator.new
    play_button['command'] = animator.play

    @lambda f: timeline_scale.config(command=f)
    def timeline_callback(value):
        animator.show(float(value) / 100 * animator.max_time())

    root.mainloop()
