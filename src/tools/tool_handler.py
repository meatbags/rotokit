import Tkinter as tk
from src.tools.tool_box import ToolBox
from src.tools.tool_path import ToolPath
from src.config import Config

class ToolHandler:
    def __init__(self, root, command):
        # commands
        self.command = command

        # vars
        self.currentTool = None
        self.frameAttributesText = tk.StringVar()

        # tool path
        self.toolPath = ToolPath()
        
        # layout
        self.frameSide = tk.Frame(root.side, borderwidth=4, relief=tk.SUNKEN)
        self.frameSide.pack(side=tk.TOP, fill=tk.X)
        self.frameLower = tk.Frame(root.mainLower, borderwidth=4, relief=tk.SUNKEN)
        self.frameLower.pack(side=tk.TOP, fill=tk.X)
        self.frameAttributes = tk.Frame(root.mainUpper, borderwidth=4, relief=tk.SUNKEN)
        self.frameAttributes.pack(side=tk.TOP, fill=tk.X)
        self.frameAttributesLabel = tk.Label(self.frameAttributes, textvariable=self.frameAttributesText)
        self.frameAttributesLabel.pack(side=tk.TOP)

        # toolbars
        self.toolBoxDraw = ToolBox(self.frameSide, 'Draw', self.onChange, tools=Config['Tools']['Draw'], radio=True, columns=2)
        self.toolsTransfer = ToolBox(self.frameLower, 'Transfer', self.onChange, tools=Config['Tools']['Transfer'])
        self.toolsMatch = ToolBox(self.frameLower, 'Match', self.onChange, tools=Config['Tools']['Match'])

    def onChange(self, toolBox, tool):
        self.command(toolBox, tool)

    def setToolFromKey(self, id):
        self.toolBoxDraw.setTool(id)
        self.setTool(id)

    def setTool(self, id):
        self.currentTool = id
        self.frameAttributesText.set(id)

    def updateToolPath(self, mouse):
        self.toolPath.trace(mouse.x, mouse.y)

    def clearToolPath(self):
        self.toolPath.clear()
