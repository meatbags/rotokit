from src.maths import Transform

class Path:
    def __init__(self, id):
        self.id = id
        self.objects = []
        self.drawFrom = 0
        self.selected = False
        self.transform = Transform()

    def addObject(self, object):
        self.objects.append(object)

    def select(self):
        self.selected = True
