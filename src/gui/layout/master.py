import tkinter as tk
from src.gui.event import Events
from src.gui.layout.pane import Pane
from src.gui.layout.toolbar import ToolBar
from src.gui.layout.canvas import Workspace
from src.gui.layout.layers import LayerFrame
from src.gui.layout.timeline import Timeline
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
        self.timeline = Timeline(self.main)
        self.workspace = Workspace(self.viewer)

        # side bar
        self.sidebar = Pane(self, orient=tk.VERTICAL)
        self.toolbar = ToolBar(self.sidebar)
        self.colourPicker = Pane(self.sidebar, label='Colour')
        self.layerFrame = LayerFrame(self.sidebar)

        # frames
        self.frameA = Frame('Frame_A', self.workspace.canvasLeft)
        self.frameB = Frame('Frame_B', self.workspace.canvasRight)
        self.frameA.addLayerList(self.layerFrame.left)
        self.frameB.addLayerList(self.layerFrame.right)

        self.frameA.draw()
        self.frameB.draw()

        # events
        #self.events = Events(self.workspace.canvasLeft, self.workspace.canvasRight)
        #self.events.bindMouseDown(self.onMouseDown)
