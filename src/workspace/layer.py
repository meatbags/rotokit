from src.interface.config import *
from src.interface.maths import Transform
import random

class Layer:
    def __init__(self, frame, id):
        self.parent = frame.id
        self.id = id
        self.requiresDraw = True
        self.hidden = False
        self.transform = Transform()

        # test
        self.colour = '#000000'
        self.lineWidth = 2
        self.start = ((random.random() * 3 - 1) * size[0], random.random() * size[1])
        self.end = ((random.random() * 3 - 1) * size[0], random.random() * size[1])

    def draw(self, canvas):
        if self.requiresDraw:
            self.requiresDraw = False
            canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1], fill=self.colour, width=self.lineWidth, smooth=1)

    def addObject(self, object):
        pass
