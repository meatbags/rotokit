from src.config import Config
import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, root, id, **kw):
        super().__init__(root, kw)
        self.config(width=Config['Canvas']['DefaultSize'][0], height=Config['Canvas']['DefaultSize'][1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=Config['Canvas']['Padding']['x'], pady=Config['Canvas']['Padding']['y'])

    def clear(self):
        canvas.delete('all')

    def draw(self, frame):
        frame.draw(self)
