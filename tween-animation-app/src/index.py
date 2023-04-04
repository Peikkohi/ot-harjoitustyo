from tkinter import *
from tkinter import ttk

from animator import Animator, AnimationHandler

root = Tk()

canvas = Canvas(root, width=800, height=600, bg='white')
canvas.grid(row=0, column=0)

obj = canvas.create_rectangle((0, 0), (100, 100), fill='green')

animator = Animator((0, 0))
animator.add_frame((300, 300))
animator.add_frame((600, 0))

animation_handler = AnimationHandler(animator,
        lambda x, y: canvas.moveto(obj, x, y), canvas.after)

frame = ttk.Frame(root)
frame.grid(row=0, column=1)

subframe = ttk.Frame(root)
subframe.grid(row=1, column=0)

ttk.Button(subframe, text='Animate', command=animation_handler.toggle).pack()

root.mainloop()
