from src.maths.vector import Vector

class BoundingBox:
    def __init__(self, points=[]):
        if len(points) == 0:
            self.min = Vector(0, 0)
            self.max = Vector(0, 0)
        else:
            self.min = Vector(min([p.x for p in points]), min([p.y for p in points]))
            self.max = Vector(max([p.x for p in points]), max([p.y for p in points]))
        self.width = self.max.x - self.min.x
        self.height = self.max.y - self.min.y

    def set(self, points):
        if len(points) == 0:
            self.min = Vector(0, 0)
            self.max = Vector(0, 0)
        else:
            self.min = Vector(min([p.x for p in points]), min([p.y for p in points]))
            self.max = Vector(max([p.x for p in points]), max([p.y for p in points]))
        self.width = self.max.x - self.min.x
        self.height = self.max.y - self.min.y
