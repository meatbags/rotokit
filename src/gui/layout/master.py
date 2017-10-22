import tkinter as tk
from src.gui.layout.toolbar import ToolBar
from src.gui.layout.pane import Pane
from src.gui.layout.canvas import Workspace
from src.gui.event import Events

class Master(tk.PanedWindow):
    def __init__(self, root):
        # master pane
        super().__init__(root)
        self.config(orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)

        # main window
        self.main = Pane(self, orient=tk.VERTICAL)
        self.attributes = Pane(self.main, label='Attributes')
        self.viewer = Pane(self.main)
        self.timeline = Pane(self.main, label='Timeline')
        self.workspace = Workspace(self.viewer)

        # side bar
        self.sidebar = Pane(self, orient=tk.VERTICAL)
        self.toolbar = ToolBar(self.sidebar)
        self.layers = Pane(self.sidebar, label='Layers')

        # events
        self.events = Events(self.workspace.canvasLeft, self.workspace.canvasRight)
        self.events.bindMouseDown(self.onMouseDown)

        # pack
        self.pack(fill=tk.BOTH, expand=1)

    def onMouseDown(self, event):
        print(event)
