from src.maths.vector import Vector

class WeightedPoint(Vector):
    def __init__(self, x, y, weight):
        Vector.__init__(self, x, y)
        self.weight = weight
