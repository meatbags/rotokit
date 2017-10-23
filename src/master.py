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

        # layout
        self.createLayout()

        # tools
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

    def createLayout(self):
        # main window
        self.main = Pane(self, orient=tk.VERTICAL)

        # tool attributes
        #self.attributes = Pane(self.main, label='Attributes')

        # upper
        self.mainUpper = Pane(self.main)
        #self.mainUpperInner = tk.Frame(self.mainUpper)
        #self.mainUpper.add(self.mainUpperInner)
        self.workspace = Workspace(self.mainUpper)

        # lower
        self.mainLower = Pane(self.main)
        self.mainLowerInner = tk.Frame(self.mainLower)
        self.mainLower.add(self.mainLowerInner)

        # sidebar
        self.sidebar = Pane(self, orient=tk.VERTICAL)
        self.sidebarInner = tk.Frame(self.sidebar)
        self.sidebar.add(self.sidebarInner)

    def createTools(self):
        self.toolBarSide = tk.Frame(self.sidebarInner)
        self.toolBarSide.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.toolBarLower = tk.Frame(self.mainLowerInner)
        self.toolBarLower.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.toolsDraw = ToolBox(self.toolBarSide, 'ToolBox_Draw', self.onToolBoxChange, tools=[tool for tool in Config['Tools']['Draw']], radio=True, columns=2)
        self.toolsTransfer = ToolBox(self.toolBarLower, 'ToolBox_Transfer', self.onToolBoxChange, tools=[tool for tool in Config['Tools']['Transfer']])
        self.toolsMatch = ToolBox(self.toolBarLower, 'ToolBox_Match', self.onToolBoxChange, tools=[tool for tool in Config['Tools']['Match']])

        self.colourPicker = Pane(self.sidebar, label='Colour')

    def onToolBoxChange(self, toolbox, tool):
        # events passed up to master
        pass

    def onLayerChange(self):
        pass
