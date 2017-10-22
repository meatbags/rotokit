
class Bezier:
    def __init__(self, p1, p2, cp1, cp2):
        self.p1 = p1
        self.p2 = p2
        self.cp1 = cp1
        self.cp2 = cp2
        self.fill = 'black'

    def draw(self, canvas, tag):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=self.fill, tags=tag)
