from src.config import Config
import Tkinter as tk
from src.event import EventHandler
from src.canvas.renderer import Renderer

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

        # render
        self.renderer = Renderer(self.size)

    def drawToolPath(self, toolPath):
        pass

    def clear(self):
        self.renderer.clear(self)

    def draw(self, frame):
        if not frame.soloMode:
            self.renderer.render(self, frame)
        else:
            self.renderer.clear(self)
            if not frame.soloLayer.hidden:
                self.renderer.renderLayer(self, frame.soloLayer)



'''
if len(toolPath.points) > 1:
    # draw path
    points = []
    lines = 0
    for i in range(toolPath.drawIndex, len(toolPath.points), 1):
        points.extend([toolPath.points[i].x, toolPath.points[i].y])
        lines += 1
    toolPath.drawIndex = i
    self.create_line(points, tags=self.toolTag)

    # draw bounding box
    box = toolPath.boundingBox
    self.delete(self.toolBoxTag)
    self.create_rectangle(box.min.x, box.min.y, box.max.x, box.max.y, outline='black', fill='', tags=self.toolBoxTag)
else:
    self.delete(self.toolTag)
    self.delete(self.toolBoxTag)
'''
