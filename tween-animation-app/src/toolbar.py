from tkinter import ttk

from root import root
from canvas import toggle

frame = ttk.Frame(root)
grid = frame.grid

button = ttk.Button(frame, text='Animate', command=toggle)
button.pack()
