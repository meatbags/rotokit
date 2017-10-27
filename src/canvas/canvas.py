from src.config import Config
import Tkinter as tk
from src.event import EventHandler
from src.frame import Layer
from src.canvas.canvas_renderer import CanvasRenderer
from src.frame import Path
from src.frame.path_objects import BezierCurve
from src.maths import Vector

class Canvas(tk.Canvas):
    def __init__(self, root, id, onMouseDown, onMouseMove, onMouseRelease, **kw):
        tk.Canvas.__init__(self, root, kw)
        self.id = str(id)
        self.size = Config['Canvas']['DefaultSize']
        self.config(width=self.size[0], height=self.size[1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=Config['Canvas']['Padding']['x'], pady=Config['Canvas']['Padding']['y'])

        # events
        self.events = EventHandler(self)
        self.events.bindMouseDown(lambda event: onMouseDown(self, self.events.mouse))
        self.events.bindMouseMove(lambda event: onMouseMove(self, self.events.mouse))
        self.events.bindMouseRelease(lambda event: onMouseRelease(self, self.events.mouse))

        # helper
        self.tags = []
        self.toolTag = self.id + '_Tool'
        self.toolBoxTag = self.id + '_Tool_BoundingBox'

        # renderer
        self.renderer = CanvasRenderer(self.size)

        # fixed tool layer
        self.toolLayer = Layer(self, self.id + '_Tool', '', self.size)
        self.toolLayer.clear()

    def drawToolPath(self, toolPath):
        if len(toolPath.points) > 1:
            # get points from tool path
            points = []
            lines = 0
            for i in range(toolPath.drawIndex, len(toolPath.points), 1):
                points.extend([toolPath.points[i].x, toolPath.points[i].y])
                lines += 1
            toolPath.drawIndex = i

            # create path and flag for draw
            if len(self.toolLayer.paths) == 0:
                self.toolLayer.addPath(Path('temp'))
            else:
                self.toolLayer.requiresPartialDraw = True

            # add new line
            self.toolLayer.paths[0].addObject(
                BezierCurve(
                    Vector(points[-2], points[-1]),
                    Vector(points[-4], points[-3]),
                    Vector(points[-2], points[-1]),
                    Vector(points[-4], points[-3])
                )
            )
            
            # draw
            self.renderer.renderLayer(self, self.toolLayer)
        else:
            self.renderer.hideLayer(self, self.toolLayer)
            self.toolLayer.clear()

    def clear(self):
        self.renderer.clear(self)

    def draw(self, frame):
        if not frame.soloMode:
            self.renderer.render(self, frame)
        else:
            self.renderer.clear(self)
            if not frame.soloLayer.hidden:
                self.renderer.renderLayer(self, frame.soloLayer)
