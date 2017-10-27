class Path:
    def __init__(self, id):
        self.id = id
        self.objects = []
        self.drawFrom = 0

    def addObject(self, object):
        self.objects.append(object)
