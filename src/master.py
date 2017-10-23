import tkinter as tk
from src.config import *
from src.core import *
from src.frame import *
from src.gui import *

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
        self.sidebarInner = tk.Frame(self.sidebar)
        self.sidebarInner.pack(side=tk.LEFT)
        self.sidebar.add(self.sidebarInner)

        self.createTools()


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

    def createTools(self):
        self.drawTools = ToolBox(
            self.sidebarInner,
            tools=[tool for tool in Config['Tools']['Draw']],
            radio=1,
            columns=2
        )
        self.colourPicker = Pane(self.sidebar, label='Colour')
