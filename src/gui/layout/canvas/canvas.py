from src.config import Config
import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, root, size=Config['Canvas']['DefaultSize']):
        super().__init__(root)

        self.conf = Config['Canvas']
        self.config(width=size[0], height=size[1], bg=self.conf['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=self.conf['Padding']['x'], pady=self.conf['Padding']['y'])

    def draw(self, frame, camera):
        for layer in frame.layers:
            layer.draw(self)
