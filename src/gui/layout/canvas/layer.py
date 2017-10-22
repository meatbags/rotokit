from src.config import Config
from src.maths import Transform
import random
import tkinter as tk

class Layer:
    def __init__(self, frame, id, size=Config['Canvas']['DefaultSize']):
        self.parent = frame.id
        self.id = id
        self.name = 'Layer ' + id
        self.requiresDraw = True
        self.hidden = tk.IntVar()

        # transform
        self.transform = Transform()

        # test
        self.colour = '#000000'
        self.lineWidth = 2
        self.start = ((random.random() * 3 - 1) * size[0], random.random() * size[1])
        self.end = ((random.random() * 3 - 1) * size[0], random.random() * size[1])

    def draw(self, canvas):
        if self.requiresDraw:
            self.requiresDraw = False
            canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1], fill=self.colour, width=self.lineWidth)

    def addButton(self, root):
        self.button = tk.Frame(root, borderwidth=4, relief=tk.SUNKEN)
        self.button.pack(side=tk.BOTTOM)
        self.buttonLabel = tk.Label(self.button, text=self.id)
        self.buttonLabel.pack(side=tk.LEFT)
        self.buttonHide = tk.Checkbutton(self.button, variable=self.hidden, text='( )', indicatoron=False)
        self.buttonHide.pack(side=tk.LEFT)

    def addObject(self, object):
        pass
