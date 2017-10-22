from src.interface.maths.vector import *
import maths

class Transform:
    def __init__(self):
        self.anchor = Vector(0, 0)
        self.position = Vector(0, 0)
        self.rotation = 0
        self.scale = Vector(1, 1)

    def rotate(points):
        for p in points:
            x = p.x - self.anchor.x
            y = p.y - self.anchor.y
            angle = math.atan2(y, x)
            mag = math.sqrt(x * x + y * y)
            p.x = math.cos(angle + self.rotation) * mag
            p.y = math.sin(angle + self.rotation) * mag
