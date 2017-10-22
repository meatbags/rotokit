import tkinter as tk
from src.interface.sidebar.toolbar import *
from src.interface.layout.pane import *
from src.interface.workspace.workspace import *
from src.interface.workspace.timeline import *
from src.interface.events.events import *
from src.interface.layers.layerrow import *

class Layout(tk.PanedWindow):
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

        # layers
        self.layersPane = Pane(self, orient=tk.VERTICAL)
        self.layerButtons = [LayerRow(self.layersPane) for layer in self.workspace.frameLeft.layers]
        
        # events
        self.events = Events(self.workspace.canvasLeft, self.workspace.canvasRight)
        self.events.bindMouseDown(self.onMouseDown)

        # pack
        self.pack(fill=tk.BOTH, expand=1)

    def onMouseDown(self, event):
        print(event)
