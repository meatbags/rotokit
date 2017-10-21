import tkinter as tk
from src.interface.config import *
from src.interface.workspace.canvas import *
from src.interface.workspace.frame import *
from src.interface.workspace.camera import *

class Workspace(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.conf = Config['Workspace']

        self.size = self.conf['DefaultSize']
        self.config(width=self.size[0], height=self.size[1])
        self.pack(fill=tk.BOTH)

        # set up
        self.camera = Camera()
        self.canvasLeft = Canvas(self)
        self.canvasRight = Canvas(self)
        self.frameLeft = Frame()
        self.frameRight = Frame()

        # run
        self.draw()
        root.add(self)

    def draw(self):
        self.canvasLeft.draw(self.frameLeft, self.camera)
        self.canvasRight.draw(self.frameRight, self.camera)
