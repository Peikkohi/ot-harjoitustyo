import tkinter as tk

from animator import Animator

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        render_frame = tk.Frame(self)
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


class Setting:
    def __init__(self, obj, settings, timeline, animation):
        self.animation = animation
        self.settings = settings
        self.obj = obj

        self.frame = tk.LabelFrame(settings)
        self.button = tk.Button(timeline, command=self.switch)
        self.button.pack(side='left')

    def switch(self):
        for widget in self.settings.slaves():
            widget.pack_forget()
        self.frame.pack()
        self.animation.show(self.obj.index)

    @staticmethod
    def frame(obj, settings, timeline, animation):
        self = Setting(obj, settings, timeline, animation)

        self.frame.config(text=f'Frame { self.obj.index }')
        self.button.config(text=self.obj.index)
        
        scale_x = tk.Scale(self.frame, to=800, orient='horizontal')
        scale_x.pack()
        
        @lambda f: scale_x.config(command=f)
        def update(value):
            obj.x = int(value)

        scale_y = tk.Scale(self.frame, to=600, orient='horizontal')
        scale_y.pack()

        @lambda f: scale_y.config(command=f)
        def update(value):
            obj.y = int(value)

    @staticmethod
    def tween(obj, settings, timeline, animation):
        self = Setting(obj, settings, timeline, animation)

        self.frame.config(text=f'Tween { self.obj.index }')
        self.button.config(text='...')

        def update(value):
            obj.current = value

        options = obj.options
        option_menu = tk.OptionMenu(self.frame,
                                    tk.Variable(), *options, command=update)
        option_menu.pack()

class Manager:
    def __init__(self, settings, timeline, schedule, position):
        self.settings = settings
        self.timeline = timeline
        self.schedule = schedule
        self.position = position

    def setting(self, animation, obj, is_tween=False):
        if is_tween:
            Setting.tween(obj, self.settings, self.timeline, animation)
        else:
            Setting.frame(obj, self.settings, self.timeline, animation)

