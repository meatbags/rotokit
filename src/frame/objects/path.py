from src.maths import Vector
from src.frame.objects.bezier_curve import Bezier
import random

class Path:
    def __init__(self, parent, id):
        self.parent = parent
        self.id = id

        bez = Bezier(
            Vector(random.random() * 100, random.random() * 100),
            Vector(random.random() * 100, random.random() * 100),
            Vector(random.random() * 100, random.random() * 100),
            Vector(random.random() * 100, random.random() * 100)
        )

        self.bezierCurves = [bez]
        self.requiresDraw = True

    def draw(self, canvas, tag):
        if self.requiresDraw:
            for bez in self.bezierCurves:
                bez.draw(canvas, tag)
            self.requiresDraw = False
