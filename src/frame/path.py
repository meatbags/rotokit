from src.maths import Transform
from src.core import Profile
from src.config import Config

class Path:
    def __init__(self, id):
        self.id = id
        self.objects = []
        self.drawFrom = 0
        self.selected = False
        self.transform = Transform()
        self.profile = Profile(self)

        # animation
        self.origin = None
        self.destination = None

        # easing
        self.easing = Config.core.easing.default

    def getPoints(self, time):
        # time should be [-1, 1]
        t = time
        pass

    def updateProfile(self):
        self.profile.path(self)

    def updateGroup(self, group):
        self.profile.group(group)

    def addObject(self, object):
        self.objects.append(object)

    def select(self):
        self.selected = True
