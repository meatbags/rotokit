TYPE_BEZIER_CURVE = 'TYPE_BEZIER_CURVE'

class BezierCurve:
    def __init__(self, p1, p2, cp1, cp2):
        self.type = TYPE_BEZIER_CURVE
        self.p1 = p1
        self.p2 = p2
        self.cp1 = cp1
        self.cp2 = cp2
        self.fill = 'black'

    def getPoints(self):
        # return pointlist
        pass
