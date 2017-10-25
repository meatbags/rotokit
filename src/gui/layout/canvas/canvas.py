from src.config import Config
import tkinter as tk
from src.gui.event import Events
from src.frame.layer import Layer

class Canvas(tk.Canvas):
    def __init__(self, root, id, onMouseDown, onMouseMove, onMouseRelease, **kw):
        super().__init__(root, kw)
        self.id = str(id)
        self.config(width=Config['Canvas']['DefaultSize'][0], height=Config['Canvas']['DefaultSize'][1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=Config['Canvas']['Padding']['x'], pady=Config['Canvas']['Padding']['y'])

        # events
        self.events = Events(self)
        self.events.bindMouseDown(lambda event: onMouseDown(self, self.events.mouse))
        self.events.bindMouseMove(lambda event: onMouseMove(self, self.events.mouse))
        self.events.bindMouseRelease(lambda event: onMouseRelease(self, self.events.mouse))

        # tool layer
        self.toolLayer = Layer(self, self.id + '_TOOL', '')
        self.toolLayer.clear(self)

    def drawTools(self, tool):
        self.toolLayer.draw(self)

    def clear(self):
        canvas.delete('all')

    def draw(self, frame):
        frame.draw(self)
