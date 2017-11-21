import Tkinter as tk
from src.config import Config
from src.canvas.canvas_renderer import CanvasRenderer

class PreviewCanvas(tk.Canvas):
    def __init__(self, root, id, **kw):
        tk.Canvas.__init__(self, root, kw)
        self.id = str(id)
        self.size = Config['PreviewCanvas']['DefaultSize']
        self.config(width=self.size[0], height=self.size[1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=2, pady=2)

        # renderer
        self.renderer = CanvasRenderer(self.size)

    def clear(self):
        self.renderer.clear(self)

    def draw(self, frame):
        pass
