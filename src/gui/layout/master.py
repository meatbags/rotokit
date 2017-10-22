import tkinter as tk
from src.gui.event import Events
from src.gui.layout.pane import Pane
from src.gui.layout.toolbar import ToolBar
from src.gui.layout.canvas import Workspace
from src.gui.layout.layers import LayersPane
from src.frame import Frame

class Master(tk.PanedWindow):
    def __init__(self, root):
        # master pane
        super().__init__(root)
        self.config(orient=tk.HORIZONTAL, sashpad=5)
        self.pack()

        # main window
        self.main = Pane(self, orient=tk.VERTICAL)
        self.attributes = Pane(self.main, label='Attributes')
        self.viewer = Pane(self.main)
        self.timeline = Pane(self.main, label='Timeline')
        self.workspace = Workspace(self.viewer)

        # side bar
        self.sidebar = Pane(self, orient=tk.VERTICAL)
        self.toolbar = ToolBar(self.sidebar)
        self.layersPane = LayersPane(self.sidebar)

        # frames
        self.frameA = Frame('frame_a')
        self.frameB = Frame('frame_b')
        self.frameA.addButtons(self.layersPane.left)
        self.frameB.addButtons(self.layersPane.right)

        # events
        self.events = Events(self.workspace.canvasLeft, self.workspace.canvasRight)
        self.events.bindMouseDown(self.onMouseDown)

    def onMouseDown(self, event):
        print(event)
