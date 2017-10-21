from src.interface.config import *
import random

class Layer:
    def __init__(self, size=Config['Canvas']['DefaultSize']):
        self.colour = '#000000'
        self.lineWidth = 2
        self.start = ((random.random() * 3 - 1) * size[0], random.random() * size[1])
        self.end = ((random.random() * 3 - 1) * size[0], random.random() * size[1])
        self.requiresDraw = True

    def draw(self, canvas):
        canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1], fill=self.colour, width=self.lineWidth, smooth=1)
