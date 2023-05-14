import tkinter as tk

from animation_player import AnimationPlayer


class AnimationPlayerAdapter:
    def __init__(self, player: AnimationPlayer, canvas: tk.Canvas):
        self.player = player
        self.canvas = canvas
        self.drawable = canvas.create_oval(0, 0, 50, 50, fill='green')

    def animate(self):
        pos_x, pos_y, is_on = self.player.next_position()
        self.canvas.moveto(self.drawable, pos_x, pos_y)
        if is_on:
            self.canvas.after(17, self.animate)

    def play(self):
        if self.player.toggle():
            self.animate()

    def show_position_of(self, time: float, normalized=False):
        pos_x, pos_y = self.player.switch_to(time, normalized)
        self.canvas.moveto(self.drawable, pos_x, pos_y)
