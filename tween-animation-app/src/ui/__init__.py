import tkinter as tk

from animation import Animation
from animation_player import AnimationPlayer

from ui.animation_player_adapter import AnimationPlayerAdapter
from ui.setting_factory import SettingFactory

def new(widget, animation: Animation,
        adapter: AnimationPlayerAdapter, factory: SettingFactory):
    def button(text, call):
        button = tk.Button(widget, text=text, command=call)
        button.pack(side='left')
        return button
    def caller(widget, time):
        def wrap():
            factory.change_shown(widget)
            adapter.show_position_of(time)
        return wrap
    def new():
        keyframe, inbetween = animation.create_keyframe()
        if inbetween is not None:
            call = caller(factory.for_inbetween(inbetween),
                    inbetween.timestamp)
            button(text='...', call=call)
        call = caller(factory.for_keyframe(keyframe), keyframe.timestamp)
        button(text=str(keyframe.timestamp), call=call)
    return new

def run_app():
    """Opens an application window and start a application loop.
    """
    root = tk.Tk()

    render_frame = tk.Frame(root)
    render_frame.pack(side='top', fill='x')

    canvas = tk.Canvas(render_frame, width=800, height=600, bg='white')
    canvas.pack(side='left')

    settings_frame = tk.Frame(render_frame)
    settings_frame.pack(side='left', fill='both')

    timeline_scale = tk.Scale(root, orient='horizontal', showvalue=False)
    timeline_scale.pack(side='top', fill='x')

    toolbar_frame = tk.Frame(root)
    toolbar_frame.pack(side='top', fill='x')

    select_frame = tk.Frame(toolbar_frame)
    select_frame.pack(side='left', fill='x', expand=True)

    chooser_frame = tk.Frame(select_frame)
    chooser_frame.pack(side='left')

    new_button = tk.Button(select_frame, text='new')
    new_button.pack(side='left')

    play_button = tk.Button(toolbar_frame, text='play')
    play_button.pack(side='right', fill='x')

    animation = Animation()
    player = AnimationPlayer(animation)

    adapter = AnimationPlayerAdapter(player, canvas)
    factory = SettingFactory(settings_frame)

    new_button['command'] = new(chooser_frame, animation, adapter, factory)
    timeline_scale['command'] = lambda value: adapter.show_position_of(
            float(value), normalized=True)
    play_button['command'] = adapter.play

    root.mainloop()


def structure(root):
    """Defines the structure of application window.

    Populates the argument root, with render, setting and toolbar area.

    Args:
        root: tkinter widget where the widgets are to be populated

    Returns:
        Widgets, which are needed for the application interaction
    """
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
    """Adds animation controlling interaction to widgets

    Initializes animation control, which provides the widgets ability to
    add new frames to the animation, control current sequence of animation.
    """
    manager = Manager(
        settings_frame, timeline_frame,
        lambda update: canvas.after(17, update),
        lambda pos: canvas.moveto(drawable, *pos),
    )
    animation_control = TEMP(manager)

    new_button['command'] = animation_control.new
    play_button['command'] = animation_control.play
    timeline_scale['command'] = lambda value: \
        animation_control.show(float(value), normalize=True)
