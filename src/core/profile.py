from src.config import Config
from src.maths import Vector
import math

class Profile:
    def __init__(self, path):
        self.path(path)

    def path(self, path):
        print('profiling')
        # get geometric features
        self.length = sum(bez.length for bez in path.objects)
        self.minX = min(min(bez.p1.x, bez.p2.x) for bez in path.objects)
        self.minY = min(min(bez.p1.y, bez.p2.y) for bez in path.objects)
        self.maxX = max(max(bez.p1.x, bez.p2.x) for bez in path.objects)
        self.maxY = max(max(bez.p1.y, bez.p2.y) for bez in path.objects)
        self.width = self.maxX - self.minX
        self.height = self.maxY - self.minY
        self.x = self.minX + self.width / 2
        self.y = self.minY + self.height / 2

    def group(self, g):
        # get centre of mass of group
        COMX = sum(path.profile.x * path.profile.length for path in g) / sum(path.profile.length for path in g)
        COMY = sum(path.profile.y * path.profile.length for path in g) / sum(path.profile.length for path in g)

        # vector to COM
        self.toCentre = Vector(self.x - COMX, self.y - COMY)
        self.magnitudeToCentre = self.toCentre.getMagnitude()

    def compare(self, profile):
        # compare profiles (lower score = more similar)
        centreOfMass = (profile.magnitudeToCentre - self.magnitudeToCentre) * Config['Core']['Weight']['CentreOfGravity']
        length = (profile.length - self.length) * Config['Core']['Weight']['Length']

        # get search magnitude
        mag = math.sqrt(pow(centreOfMass, 2) + pow(length, 2))

        return mag
