from src.config import Config
from src.maths import WeightedPoint, Vector, BoundingBox

class ToolPath:
    def __init__(self):
        self.points = []
        self.position = Vector(0, 0)
        self.float = Vector(0, 0)
        self.floatRadius = Config['Tool']['FloatRadius']
        self.threshold = 1
        self.boundingBox = BoundingBox(self.points)
        self.boundingBoxInner = BoundingBox(self.points)
        self.drawIndex = 0

    def beginPath(self, x, y):
        # begin tracking tool

        self.position.x = self.float.x = x
        self.position.y = self.float.y = y
        self._addPoint(x, y)

    def moveTo(self, x, y):
        # move to point, draw if outside radius

        self.position.x = x
        self.position.y = y
        distance = self.float.distanceTo(self.position)

        if distance > self.floatRadius:
            self.float.extend(self.float.angleTo(self.position), distance - self.floatRadius)
            self._addPoint(self.float.x, self.float.y)

    def clearPath(self):
        self.points = []
        self.drawIndex = 0
        self.boundingBox.set(self.points)
        self.boundingBoxInner.set(self.points)

    def _addPoint(self, x, y):
        # add a new point to path

        point = WeightedPoint(x, y, 1)
        self.lastPoint = point
        self.points.append(point)
        self.boundingBox.set(self.points)
        self.boundingBoxInner.set([self.points[0], self.points[-1]])
