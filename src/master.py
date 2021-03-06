import Tkinter as tk
from src.canvas import *
from src.config import *
from src.core import *
from src.frame import *
from src.gui import *
from src.tools import *

class Master(tk.Frame):
    def __init__(self, root, **kw):
        # master pane
        tk.Frame.__init__(self, root, **kw)
        self.pack(fill=tk.BOTH, expand=1)

        # set up
        self.createLayout()
        self.createHandlers()

        # events
        self.setEvents()

    def createLayout(self):
        # main window
        self.main = tk.Frame(self, borderwidth=4, relief=tk.SUNKEN)
        self.main.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.mainUpper = tk.Frame(self.main)
        self.mainUpper.pack(side=tk.TOP, fill=tk.X)
        self.mainLower = tk.Frame(self.main)
        self.mainLower.pack(side=tk.BOTTOM, fill=tk.X, expand=1)

        # side bar
        self.side = tk.Frame(self)
        self.side.pack(side=tk.RIGHT, fill=tk.Y)

    def createHandlers(self):
        # toolbars
        self.toolHandler = ToolHandler(self, self.handleToolChange)

        # timeline
        self.timeline = Timeline(self.side, self.handleTimelineChange)

        # layers
        self.layerList = LayerList(self.side, self.handleLayerListChange)

        # frames
        self.frameHandler = FrameHandler()
        self.frameHandler.addFrame('Frame_0', 'Frame_1', 'Frame_2')

        # add frames to timeline
        self.timeline.addFrames(self.frameHandler.frames)
        self.timeline.setActiveFrames(self.frameHandler.activeFrames)

        # add layer lists
        self.layerList.setActiveFrames(self.frameHandler.activeFrames)

        # canvas
        self.canvasHandler = CanvasHandler(self.mainUpper, self.handleCanvasMouseDown, self.handleCanvasMouseMove, self.handleCanvasMouseRelease)
        self.canvasHandler.drawFrames(self.frameHandler.activeFrames)

    def isSpecialKeyDown(self):
        specialKeysDown = sum([1 for key in self.specialKeys if self.specialKeys[key] == True])

        return (specialKeysDown > 0)

    def setEvents(self):
        self.specialKeys = {
            'Shift': False,
            'Ctrl': False,
            'Alt': False
        };

        def setSpecialKey(key, value):
            self.specialKeys[key] = value

        def setToolFromKey(key):
            if not self.isSpecialKeyDown():
                self.toolHandler.setToolFromKey(Config['Tools']['Draw'][key])

        self.keyDown = {
            'Shift_R': (lambda e: setSpecialKey('Shift', True)),
            'Shift_L': (lambda e: setSpecialKey('Shift', True)),
            'Control_R': (lambda e: setSpecialKey('Ctrl', True)),
            'Control_L': (lambda e: setSpecialKey('Ctrl', True)),
            'Alt_R': (lambda e: setSpecialKey('Alt', True)),
            'Alt_L': (lambda e: setSpecialKey('Alt', True)),
            'h': (lambda e: setToolFromKey('Hand')),
            'v': (lambda e: setToolFromKey('Select')),
            't': (lambda e: setToolFromKey('Transform')),
            'z': (lambda e: setToolFromKey('Zoom')),
            'p': (lambda e: setToolFromKey('Pen')),
            'b': (lambda e: setToolFromKey('Brush')),
            's': (lambda e: setToolFromKey('Sculpt')),
            'm': (lambda e: setToolFromKey('Mask'))
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

    def handleToolChange(self, toolbox, tool):
        self.toolHandler.setTool(tool.id)
        print(toolbox.id, tool.id)

        if tool.id == Config['Tools']['Preview']['Render']:
            self.canvasHandler.drawPreview(self.frameHandler.activeFrames)

    def handleCanvasMouseDown(self, canvas, mouse):
        self.canvasHandler.setActiveCanvas(canvas.id)
        self.frameHandler.setActiveFrame(self.canvasHandler.activeCanvasIndex)
        self.toolHandler.beginToolPath(mouse)
        self.canvasHandler.drawToolPath(self.toolHandler.currentTool, self.toolHandler.toolPath)

    def handleCanvasMouseMove(self, canvas, mouse):
        self.toolHandler.updateToolPath(mouse)
        self.canvasHandler.drawToolPath(self.toolHandler.currentTool, self.toolHandler.toolPath)

    def handleCanvasMouseRelease(self, canvas, mouse):
        self.frameHandler.parseTool(self.toolHandler.currentTool, self.toolHandler.toolPath)
        self.toolHandler.clearToolPath()
        self.canvasHandler.drawToolPath(self.toolHandler.currentTool, self.toolHandler.toolPath)
        self.canvasHandler.drawFrames(self.frameHandler.activeFrames)

    def handleLayerListChange(self, frame, layer):
        self.canvasHandler.drawFrames(self.frameHandler.activeFrames)

    def handleTimelineChange(self, timelineFrame):
        # set active frames and redraw
        self.frameHandler.toggleFrame(timelineFrame, len(self.canvasHandler.canvasStack))
        self.timeline.setActiveFrames(self.frameHandler.activeFrames)

        # show layers list
        self.layerList.setActiveFrames(self.frameHandler.activeFrames)

        # redraw
        self.canvasHandler.clearAll()
        self.canvasHandler.drawFrames(self.frameHandler.activeFrames)

    def handleKeyDown(self, event):
        print(event.keysym)
        if event.keysym in self.keyDown:
            self.keyDown[event.keysym](event)

    def handleKeyRelease(self, event):
        if event.keysym in self.keyRelease:
            self.keyRelease[event.keysym](event)

    def handleMenuItem(self, item):
        print(item)
