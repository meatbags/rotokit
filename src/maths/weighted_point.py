from src.maths.vector import Vector

class WeightedPoint(Vector):
    def __init__(self, x, y, weight):
        super().__init__(x, y)
        self.weight = weight
