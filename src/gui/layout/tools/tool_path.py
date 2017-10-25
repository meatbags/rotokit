from src.config import Config
from src.maths import WeightedPoint, Vector, BoundingBox

class ToolPath:
    def __init__(self):
        self.points = []
        self.x = 0
        self.y = 0
        self.threshold = 1
        self.boundingBox = BoundingBox(self.points)
        self.drawIndex = 0

    def addPoint(self, x, y):
        # add a new point to path
        point = WeightedPoint(x, y, 1)
        self.lastPoint = point
        self.points.append(point)
        self.boundingBox.set(self.points)

    def trace(self, x, y):
        # check if point should be added
        point = Vector(x, y)
        if len(self.points) == 0 or not (point.x == self.lastPoint.x and point.y == self.lastPoint.y):
            self.addPoint(x, y)

    def clear(self):
        self.points = []
        self.drawIndex = 0
        self.boundingBox.set(self.points)
