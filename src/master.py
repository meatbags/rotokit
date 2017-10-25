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

        # timeline
        self.onTimelineChange = lambda frame: print(frame)
        self.timeline = Timeline(self.mainLowerInner, self.onTimelineChange)

    def createFrame(self):
        # frames
        self.frames = [Frame(name) for name in ['A', 'B', 'C', 'D', 'E']]
        self.activeFrames = [self.frames[0], self.frames[1]]

        # add frames to timeline
        self.timeline.addFrames(self.frames)

        # add layer lists
        self.layerList.addFrames(self.activeFrames)

        # canvas
        self.canvas = CanvasWorkspace(self.mainUpperInner, self.handleCanvasMouseDown, self.handleCanvasMouseMove, self.handleCanvasMouseRelease)
        self.canvas.drawFrames(self.activeFrames)

    def isSpecialKeyDown(self):
        specialKeysDown = sum([1 for key in self.specialKeys if self.specialKeys[key] == True])

        return (specialKeysDown > 0)

    def setTool(self, toolId):
        self.attributeText.set(toolId)

    def setToolFromKey(self, toolId):
        if not self.isSpecialKeyDown():
            self.toolsDraw.setTool(toolId)
            self.attributeText.set(toolId)

    def setEvents(self):
        self.specialKeys = {
            'Shift': False,
            'Ctrl': False,
            'Alt': False
        };

        def setSpecialKey(key, value):
            self.specialKeys[key] = value

        self.keyDown = {
            'Shift_R': (lambda e: setSpecialKey('Shift', True)),
            'Shift_L': (lambda e: setSpecialKey('Shift', True)),
            'Control_R': (lambda e: setSpecialKey('Ctrl', True)),
            'Control_L': (lambda e: setSpecialKey('Ctrl', True)),
            'Alt_R': (lambda e: setSpecialKey('Alt', True)),
            'Alt_L': (lambda e: setSpecialKey('Alt', True)),
            'h': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Hand'])),
            'v': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Select'])),
            't': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Transform'])),
            'z': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Zoom'])),
            'p': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Pen'])),
            'b': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Brush'])),
            's': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Sculpt'])),
            'm': (lambda e: self.setToolFromKey(Config['Tools']['Draw']['Mask']))
        }
        self.keyRelease = {
            'Shift_R': (lambda e: setSpecialKey('Shift', False)),
            'Shift_L': (lambda e: setSpecialKey('Shift', False)),
            'Control_R': (lambda e: setSpecialKey('Ctrl', False)),
            'Control_L': (lambda e: setSpecialKey('Ctrl', False)),
            'Alt_R': (lambda e: setSpecialKey('Alt', False)),
            'Alt_L': (lambda e: setSpecialKey('Alt', False))
        }
        self.keys = {
            'Shift': False,
            'Ctrl': False,
            'Alt': False
        }

    def handleCanvasMouseDown(self, canvas, mouse):
        print('DOWN', canvas.id, mouse.x, mouse.y)

    def handleCanvasMouseMove(self, canvas, mouse):
        pass
        #print(canvas, mouse)

    def handleCanvasMouseRelease(self, canvas, mouse):
        print('UP', canvas.id, mouse.x, mouse.y)

    def handleKeyDown(self, event):
        print(event.keysym)
        if event.keysym in self.keyDown:
            self.keyDown[event.keysym](event)

    def handleKeyRelease(self, event):
        if event.keysym in self.keyRelease:
            self.keyRelease[event.keysym](event)

    def handleMenuItem(self, item):
        print(item)
