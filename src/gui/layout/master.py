import tkinter as tk
from src.gui.layout.toolbar import ToolBar
from src.gui.layout.pane import Pane
from src.gui.layout.canvas import Workspace
from src.gui.layout.timeline import Timeline
from src.gui.event import Events

class Master(tk.PanedWindow):
    def __init__(self, root):
        # master pane
        super().__init__(root)
        self.config(orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)

        # side bar
        self.sidebar = Pane(self)
        self.toolbar = ToolBar(self.sidebar)

        # main window
        self.main = Pane(self, orient=tk.VERTICAL)
        self.viewer = Pane(self.main)
        self.timeline = Timeline(self.main)
        self.workspace = Workspace(self.viewer)

        # events
        self.events = Events(self.workspace.canvasLeft, self.workspace.canvasRight)
        self.events.bindMouseDown(self.onMouseDown)

        # pack
        self.pack(fill=tk.BOTH, expand=1)

    def onMouseDown(self, event):
        print(event)
