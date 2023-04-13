import tkinter as tk

from animator import Pos, scheduled, animation, drawable

if __name__ == '__main__':
    root = tk.Tk()

    canvas = tk.Canvas(root, width=800, height=600, bg='white')
    canvas.pack()

    class Handler:
        frames = [Pos(0, 0), Pos(100, 0), Pos(0, 0)]
        move_to = drawable(canvas, 0, 0, 50, 50, fill='green')
        frame = animation(frames)
        time = 0
        max_time = len(frames) - 1
        play = False

        @staticmethod
        @scheduled(root, interval=17)
        def update():
            Handler.move_to(Handler.frame(Handler.time))
            Handler.time += 0.01
            Handler.time %= Handler.max_time
            if Handler.play:
                Handler.update()

        @staticmethod
        def toggle():
            Handler.play = not Handler.play
            if Handler.play:
                Handler.update()

    button = tk.Button(root, text='Animate', command=Handler.toggle)
    button.pack()

    root.mainloop()
