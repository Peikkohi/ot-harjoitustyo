from tkinter import *
from tkinter import ttk

from root import *
from animator import Animator, AnimationHandler

canvas = Canvas(root, width=800, height=600, bg='white')

obj = canvas.create_rectangle((0, 0), (100, 100), fill='green')

animator = Animator((0, 0))
animator.add_frame((300, 300))
animator.add_frame((600, 0))

animation_handler = AnimationHandler(animator,
        lambda x, y: canvas.moveto(obj, x, y), canvas.after)

toggle = animation_handler.toggle
grid = canvas.grid
