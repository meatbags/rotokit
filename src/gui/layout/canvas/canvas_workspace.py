import tkinter as tk
from src.config import Config
from src.gui.layout.canvas.canvas import Canvas

class CanvasWorkspace(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(width=Config['Workspace']['DefaultSize'][0], height=Config['Workspace']['DefaultSize'][1])
        self.pack(fill=tk.BOTH)

        # canvas
        self.canvasStack = []
        self.addCanvas(2)

    def addCanvas(self, n):
        for i in range(n):
            id = 'Canvas_' + str(i)
            self.canvasStack.append(Canvas(self, id))

    def drawFrames(self, frames):
        for i in range(len(frames)):
            if i < len(self.canvasStack):
                self.canvasStack[i].draw(frames[i])
