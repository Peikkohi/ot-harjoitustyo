import tkinter as tk

from ui.animation_control import AnimationControl
from ui.setting_factory import Manager


def run_app():
    root = tk.Tk()

    interactive_widgets = structure(root)
    interaction(*interactive_widgets)

    root.mainloop()


def structure(root):
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

    return new_button, play_button, timeline_scale, \
        settings_frame, timeline_frame, \
        canvas, drawable


def interaction(new_button, play_button, timeline_scale,
                settings_frame, timeline_frame,
                canvas, drawable):
    manager = Manager(
        settings_frame, timeline_frame,
        lambda update: canvas.after(17, update),
        lambda pos: canvas.moveto(drawable, *pos),
    )
    animation_control = AnimationControl(manager)

    new_button['command'] = animation_control.new
    play_button['command'] = animation_control.play
    timeline_scale['command'] = lambda value: \
        animation_control.uniform_show(float(value))
