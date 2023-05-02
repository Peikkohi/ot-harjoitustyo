import tkinter as tk


class SettingFactory:
    def __init__(self, settings, timeline):
        self.settings = settings
        self.timeline = timeline

    def frame(self, animation, position):
        frame, button = self.setting(position, animation)
        frame.config(text=f'Frame { position.index }')
        button.config(text=position.index)

        scale_x = tk.Scale(frame, to=800, orient='horizontal')
        scale_x['command'] = lambda val: position.set_x(int(val))
        scale_x.pack()

        scale_y = tk.Scale(frame, to=600, orient='horizontal')
        scale_y['command'] = lambda val: position.set_y(int(val))
        scale_y.pack()

    def tween(self, animation, tween):
        frame, button = self.setting(tween, animation)
        frame['text'] = f'Tween { tween.index }'
        button['text'] = '...'
        option_menu = tk.OptionMenu(frame, tk.Variable(),
                                    *tween.options, command=tween.set_current)
        option_menu.pack()

    def setting(self, obj, animation):
        frame = tk.LabelFrame(self.settings)
        button = tk.Button(self.timeline)
        button.pack(side='left')

        @lambda f: button.config(command=f)
        def switch():
            for widget in self.settings.slaves():
                widget.pack_forget()
            frame.pack()
            animation.show(obj.index)

        return frame, button


class Manager(SettingFactory):
    def __init__(self, settings, timeline, schedule, position):
        super().__init__(settings, timeline)
        self.schedule = schedule
        self.position = position
