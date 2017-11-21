from src.maths import Transform, applyEasing
from src.core import Profile
from src.config import Config

class Path:
    def __init__(self, id):
        self.id = id
        self.objects = []
        self.drawFrom = 0
        self.selected = False
        self.transform = Transform()

        # searching
        self.profile = None

        # animation
        self.origin = None
        self.destination = None

        # easing
        self.easing = Config['Core']['Easing']['Default']

        # draw settings
        self.lineWidth = 1

    def setTween(self, time):
        # tweening between origin or destination
        # get easing [0, 1]
        t = applyEasing(self.easing, time)
        print(t)

        # tween backwards or forwards
        if time >= 0:
            if self.destination:
                pass
            else:
                self.lineWidth = 1 - t
        else:
            if self.origin:
                pass
            else:
                self.lineWidth = t

    def updateProfile(self):
        self.profile.path(self)

    def updateGroup(self, group):
        self.profile.group(group)

    def addObject(self, object):
        self.objects.append(object)

    def select(self):
        self.selected = True
