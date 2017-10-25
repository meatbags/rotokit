import tkinter as tk
from src.config import *
from src.core import *
from src.frame import *
from src.gui import *

class Master(tk.PanedWindow):
    def __init__(self, root, **kw):
        # master pane
        super().__init__(root)
        self.config(orient=tk.HORIZONTAL, sashrelief=tk.SUNKEN, sashwidth=2, **kw)
        self.pack()

        # set up
        self.createLayout()
        self.createTools()
        self.createFrame()

        # events
        self.setEvents()

    def createLayout(self):
        # master window
        self.main = Pane(self, orient=tk.VERTICAL, sashrelief=tk.SUNKEN, sashwidth=2)

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

    def createTools(self):
        # toolbars
        self.toolBarSide = tk.Frame(self.sidebarInner, borderwidth=4, relief=tk.SUNKEN)
        self.toolBarSide.pack(side=tk.TOP, fill=tk.X)
        self.toolBarLower = tk.Frame(self.mainLowerInner)
        self.toolBarLower.pack(side=tk.TOP, fill=tk.X, expand=1)

        # tools
        self.onToolBoxChange = lambda toolbox, tool: self.setTool(tool.id)
        self.toolsDraw = ToolBox(self.toolBarSide, 'Draw', self.onToolBoxChange, tools=Config['Tools']['Draw'], radio=True, columns=2)
        self.toolsTransfer = ToolBox(self.toolBarLower, 'Transfer', self.onToolBoxChange, tools=Config['Tools']['Transfer'])
        self.toolsMatch = ToolBox(self.toolBarLower, 'Match', self.onToolBoxChange, tools=Config['Tools']['Match'])

        # tool attributes
        self.attributeText = tk.StringVar()
        self.toolAttributes = tk.Label(self.mainUpperInner, textvariable=self.attributeText, borderwidth=4, relief=tk.SUNKEN)
        self.toolAttributes.pack(side=tk.TOP, fill=tk.X, expand=1)

        # colour picker
        self.colourPicker = tk.Label(self.sidebarInner, text='Colour Picker')
        self.colourPicker.pack(side=tk.TOP)

        # layers
        self.onLayerListChange = lambda frame, layer: self.canvas.drawFrames(self.frames)
        self.layerList = LayerList(self.sidebarInner, self.onLayerListChange)

    def createFrame(self):
        # frames
        self.frames = [Frame('A'), Frame('B')]

        # add layer lists
        self.layerList.addFrames(self.frames)

        # canvas
        self.canvas = CanvasWorkspace(self.mainUpperInner)
        self.canvas.drawFrames(self.frames)

    def setTool(self, toolId):
        self.toolsDraw.setTool(toolId)
        self.attributeText.set(toolId)

    def setEvents(self):
        def setKey(key, value):
            self.keys[key] = value

        self.keyDown = {
            'Shift_R': (lambda e: setKey('Shift', True)),
            'Shift_L': (lambda e: setKey('Shift', True)),
            'Control_R': (lambda e: setKey('Ctrl', True)),
            'Control_L': (lambda e: setKey('Ctrl', True)),
            'Alt_R': (lambda e: setKey('Alt', True)),
            'Alt_L': (lambda e: setKey('Alt', True)),
            'h': (lambda e: self.setTool(Config['Tools']['Draw']['Hand'])),
            'v': (lambda e: self.setTool(Config['Tools']['Draw']['Select'])),
            't': (lambda e: self.setTool(Config['Tools']['Draw']['Transform'])),
            'z': (lambda e: self.setTool(Config['Tools']['Draw']['Zoom'])),
            'p': (lambda e: self.setTool(Config['Tools']['Draw']['Pen'])),
            'b': (lambda e: self.setTool(Config['Tools']['Draw']['Brush'])),
            's': (lambda e: self.setTool(Config['Tools']['Draw']['Sculpt'])),
            'm': (lambda e: self.setTool(Config['Tools']['Draw']['Mask']))
        }
        self.keyRelease = {
            'Shift_R': (lambda e: setKey('Shift', False)),
            'Shift_L': (lambda e: setKey('Shift', False)),
            'Control_R': (lambda e: setKey('Ctrl', True)),
            'Control_L': (lambda e: setKey('Ctrl', True)),
            'Alt_R': (lambda e: setKey('Alt', True)),
            'Alt_L': (lambda e: setKey('Alt', True))
        }
        self.keys = {
            'Shift': False,
            'Ctrl': False,
            'Alt': False
        }

    def handleKeyDown(self, event):
        print(event.keysym)
        if event.keysym in self.keyDown:
            self.keyDown[event.keysym](event)

    def handleKeyRelease(self, event):
        if event.keysym in self.keyRelease:
            self.keyRelease[event.keysym](event)

    def handleMenuItem(self, item):
        print(item)
