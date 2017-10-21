from src.interface.config import *
import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, root, size=Config['Canvas']['DefaultSize']):
        super().__init__(root)

        self.config(width=size[0], height=size[1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT)

    def draw(self, frame, camera):
        self.delete('all')

        for layer in frame.layers:
            if layer.requiresDraw:
                layer.draw(self)
