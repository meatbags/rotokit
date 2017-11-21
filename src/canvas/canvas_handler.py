import Tkinter as tk
from src.config import Config
from src.canvas.canvas import Canvas
from src.canvas.preview_canvas import PreviewCanvas

class CanvasHandler(tk.Frame):
    def __init__(self, root, onMouseDown, onMouseMove, onMouseRelease):
        tk.Frame.__init__(self, root, borderwidth=4, relief=tk.SUNKEN)
        self.config(width=Config['Workspace']['DefaultSize'][0], height=Config['Workspace']['DefaultSize'][1])
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # events
        self.onMouseDown = lambda canvas, mouse: onMouseDown(canvas, mouse)
        self.onMouseMove = lambda canvas, mouse: onMouseMove(canvas, mouse)
        self.onMouseRelease = lambda canvas, mouse: onMouseRelease(canvas, mouse)

        # canvas
        self.canvasFrame = tk.Frame(self)
        self.canvasFrame.pack(side=tk.TOP, fill=tk.X)
        self.canvasStack = []
        self.addCanvas(2)

        # active canvas
        self.activeCanvas = self.canvasStack[0]
        self.activeCanvasIndex = 0

        # preview canvases
        self.previewCanvasFrame = tk.Frame(self)
        self.previewCanvasFrame.pack(side=tk.TOP, fill=tk.X, padx=Config['Canvas']['Padding']['x'])
        self.previewCanvasStack = []
        self.addPreviewCanvas(3)

    def setActiveCanvas(self, id):
        for i in range(len(self.canvasStack)):
            if self.canvasStack[i].id == id:
                self.activeCanvas = self.canvasStack[i]
                self.activeCanvasIndex = i
                break

    def clearAll(self):
        for canvas in self.canvasStack:
            canvas.clear()

    def drawToolPath(self, toolId, toolPath):
        self.activeCanvas.drawToolPath(toolId, toolPath)

    def addCanvas(self, n):
        for i in range(n):
            id = 'Canvas_' + str(i)
            self.canvasStack.append(Canvas(self.canvasFrame, id, self.onMouseDown, self.onMouseMove, self.onMouseRelease))

    def addPreviewCanvas(self, n):
        for i in range(n):
            id = 'PreviewCanvas_' + str(i)
            self.canvasStack.append(PreviewCanvas(self.previewCanvasFrame, id))

    def drawFrames(self, frames):
        for i in range(len(frames)):
            if i < len(self.canvasStack):
                self.canvasStack[i].draw(frames[i])
