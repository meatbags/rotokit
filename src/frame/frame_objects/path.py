from src.maths import Vector
from src.frame.frame_objects.bezier_curve import Bezier
import random

class Path:
    def __init__(self, parent, id):
        self.parent = parent
        self.id = id
        self.objects = []

        self.objects.append(
            Bezier(
                Vector(random.random() * 100, random.random() * 100),
                Vector(random.random() * 100, random.random() * 100),
                Vector(random.random() * 100, random.random() * 100),
                Vector(random.random() * 100, random.random() * 100)
            )
        )

        self.requiresDraw = True
