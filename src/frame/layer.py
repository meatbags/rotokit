from src.config import Config
from src.maths import Transform
import random
import tkinter as tk

class Layer:
    def __init__(self, frame, id, name):
        self.parent = frame.id
        self.id = id
        self.name = name
        self.requiresDraw = True
        self.hidden = tk.IntVar()

        # transform
        self.transform = Transform()

        # test
        self.colour = '#000000'
        self.lineWidth = 2
        self.start = (random.random() * 100, random.random() * 100)
        self.end = (random.random() * 100, random.random() * 100)

    def draw(self, canvas):
        if self.requiresDraw:
            self.requiresDraw = False
            canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1], fill=self.colour, width=self.lineWidth)

    def addButton(self, root):
        self.button = tk.Frame(root, borderwidth=4, relief=tk.SUNKEN)
        self.button.pack(side=tk.TOP, fill=tk.X)
        self.buttonLabel = tk.Label(self.button, text=self.name)
        self.buttonLabel.pack(side=tk.LEFT)
        self.buttonHide = tk.Checkbutton(self.button, variable=self.hidden, text='( )', indicatoron=False)
        self.buttonHide.pack(side=tk.RIGHT)

    def addObject(self, object):
        pass
