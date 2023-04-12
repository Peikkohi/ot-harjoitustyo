from tkinter import Canvas

from root import root
from animator import Animator, AnimationHandler, Pos

canvas = Canvas(root, width=800, height=600, bg='white')

obj = canvas.create_rectangle((0, 0), (100, 100), fill='green')

animator = Animator(Pos(x=0, y=0))
animator.add_frame(Pos(x=300, y=300))
animator.add_frame(Pos(x=600, y=0))

animation_handler = AnimationHandler(
    animator,
    lambda x, y: canvas.moveto(obj, x, y), canvas.after,
)

toggle = animation_handler.toggle
grid = canvas.grid
