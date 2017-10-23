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

        # set up
        self.createLayout()
        self.createTools()
        self.createCanvas()





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

    def createLayout(self):
        # master window
        self.main = Pane(self, orient=tk.VERTICAL)

        # upper
        self.mainUpper = Pane(self.main)
        self.mainUpperInner = tk.Frame(self.mainUpper)
        self.mainUpper.add(self.mainUpperInner)

        # lower
        self.mainLower = Pane(self.main)
        self.mainLowerInner = tk.Frame(self.mainLower)
        self.mainLower.add(self.mainLowerInner)

        # sidebar
        self.sidebar = Pane(self, orient=tk.VERTICAL)
        self.sidebarInner = tk.Frame(self.sidebar)
        self.sidebar.add(self.sidebarInner)

    def createTools(self):
        # methods
        self.onToolBoxChange = lambda toolbox, tool: print(toolbox.id, tool.id)
        self.onLayerListChange = lambda layer: print(layer.id)

        # toolbars
        self.toolBarSide = tk.Frame(self.sidebarInner)
        self.toolBarSide.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.toolBarLower = tk.Frame(self.mainLowerInner)
        self.toolBarLower.pack(side=tk.TOP, fill=tk.X, expand=1)

        # tools
        self.toolsDraw = ToolBox(self.toolBarSide, 'Draw', self.onToolBoxChange, tools=Config['Tools']['Draw'], radio=True, columns=2)
        self.toolsTransfer = ToolBox(self.toolBarLower, 'Transfer', self.onToolBoxChange, tools=Config['Tools']['Transfer'])
        self.toolsMatch = ToolBox(self.toolBarLower, 'Match', self.onToolBoxChange, tools=Config['Tools']['Match'])

        # TODO: ... ?
        self.colourPicker = Pane(self.sidebar, label='Colour')
        self.layerFrame = LayerFrame(self.sidebar)

    def createCanvas(self):
        self.workspace = Workspace(self.mainUpperInner)

    def onLayerChange(self):
        pass
