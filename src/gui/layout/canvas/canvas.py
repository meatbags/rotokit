from src.config import Config
import tkinter as tk
from src.gui.event import Events

class Canvas(tk.Canvas):
    def __init__(self, root, id, onMouseDown, onMouseMove, onMouseRelease, **kw):
        super().__init__(root, kw)
        self.id = str(id)
        self.config(width=Config['Canvas']['DefaultSize'][0], height=Config['Canvas']['DefaultSize'][1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=Config['Canvas']['Padding']['x'], pady=Config['Canvas']['Padding']['y'])

        # events
        self.events = Events(self)
        self.events.bindMouseDown(lambda event: (print(event), onMouseDown(self, self.events.mouse)))
        self.events.bindMouseMove(lambda event: onMouseMove(self, self.events.mouse))
        self.events.bindMouseRelease(lambda event: onMouseRelease(self, self.events.mouse))

        # tool helper
        self.toolTag = self.id + '_tool'
        self.toolBoxTag = self.id + '_tool_bbox'

        # label
        # self.labelText = tk.StringVar()
        # self.toolAttributes = tk.Label(root, textvariable=self.labelText)
        # self.toolAttributes.pack(side=tk.BOTTOM)

    def drawToolPath(self, toolPath):
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

    def clear(self):
        self.delete('all')

    def draw(self, frame):
        frame.draw(self)
