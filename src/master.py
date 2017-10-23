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
        self.layout()
        self.tools()
        self.frame()

    def layout(self):
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
        self.sidebarInner = tk.Frame(self.sidebar, borderwidth=4, relief=tk.SUNKEN)
        self.sidebar.add(self.sidebarInner, width=360)

    def tools(self):
        # toolbars
        self.toolBarSide = tk.Frame(self.sidebarInner, borderwidth=4, relief=tk.SUNKEN)
        self.toolBarSide.pack(side=tk.TOP, fill=tk.X)
        self.toolBarLower = tk.Frame(self.mainLowerInner)
        self.toolBarLower.pack(side=tk.TOP, fill=tk.X, expand=1)

        # tools
        self.onToolBoxChange = lambda toolbox, tool: self.attributeText.set(tool.id)
        self.toolsDraw = ToolBox(self.toolBarSide, 'Draw', self.onToolBoxChange, tools=Config['Tools']['Draw'], radio=True, columns=2)
        self.toolsTransfer = ToolBox(self.toolBarLower, 'Transfer', self.onToolBoxChange, tools=Config['Tools']['Transfer'])
        self.toolsMatch = ToolBox(self.toolBarLower, 'Match', self.onToolBoxChange, tools=Config['Tools']['Match'])

        # tool attributes
        self.attributeText = tk.StringVar()
        self.toolAttributes = tk.Label(self.mainUpperInner, textvariable=self.attributeText, borderwidth=4, relief=tk.SUNKEN)
        self.toolAttributes.pack(side=tk.TOP, fill=tk.X, expand=1)

        # colours
        self.colourPicker = tk.Label(self.sidebarInner, text='Colour Picker')
        self.colourPicker.pack(side=tk.TOP)

        # layers
        self.onLayerListChange = lambda frame, layer: self.canvas.drawFrames(self.frames)
        self.layerList = LayerList(self.sidebarInner, self.onLayerListChange)

    def frame(self):
        # frames
        self.frames = [Frame('A'), Frame('B')]

        # add layer lists
        self.layerList.addFrames(self.frames)

        # canvas
        self.canvas = CanvasWorkspace(self.mainUpperInner)
        self.canvas.drawFrames(self.frames)
