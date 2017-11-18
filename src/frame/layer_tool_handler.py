from src.frame.path import Path
from src.maths import BezierCurve, Vector

class LayerToolHandler:
    def __init__(self):
        pass

    def parse(self, toolId, toolPath, layer):
        print(toolId)

        newPath = Path(layer.uid('path'))

        for i in range(len(toolPath.points) - 1):
            p0 = toolPath.points[i]
            p1 = toolPath.points[i + 1]
            newPath.addObject(
                BezierCurve(
                    Vector(p0.x, p0.y),
                    Vector(p1.x, p1.y),
                    Vector(p0.x, p0.y),
                    Vector(p1.x, p1.y)
                )
            )

        layer.addPath(newPath)
        layer.requiresPartialDraw = True
