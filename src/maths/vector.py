import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = self.getMagnitude()

    def getMagnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def scale(self, s):
        self.x *= s
        self.y *= s

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def subtract(self, vec):
        self.x -= vec.x
        self.y -= vec.y
