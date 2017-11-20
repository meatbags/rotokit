from src.config import Config

class Profile:
    def __init__(self, path):
        self.parse(path)

    def parse(path):
        self.length = sum(bez.length for bez in path.objects)
        self.minX = min(min(bez.p1.x, bez.p2.x) for bez in path.objects),
        self.minY = min(min(bez.p1.y, bez.p2.y) for bez in path.objects)
        self.maxX = max(max(bez.p1.x, bez.p2.z) for bez in path.objects)
        self.maxY = max(max(bez.p1.y, bez.p2.y) for bez in path.objects)
        self.width = self.maxX - self.minX
        self.height = self.maxY - self.minY
        self.x = self.minX + self.width / 2
        self.y = self.minY + self.height / 2
