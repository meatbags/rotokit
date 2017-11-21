import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def extend(self, angle, distance):
        self.x += math.cos(angle) * distance
        self.y += math.sin(angle) * distance

    def distanceTo(self, vec):
        return math.sqrt(math.pow(vec.x - self.x, 2) + math.pow(vec.y - self.y, 2))

    def angleTo(self, vec):
        return math.atan2(vec.y - self.y, vec.x - self.x)
