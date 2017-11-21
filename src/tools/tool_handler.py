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
        self.frameUpper = tk.Frame(root.mainUpper)
        self.frameUpper.pack(side=tk.TOP, fill=tk.X)
        self.frameLower = tk.Frame(root.mainLower, borderwidth=4, relief=tk.SUNKEN)
        self.frameLower.pack(side=tk.TOP, fill=tk.X)
        self.frameAttributes = tk.Frame(root.mainUpper, borderwidth=4, relief=tk.SUNKEN)
        self.frameAttributes.pack(side=tk.TOP, fill=tk.X)
        self.frameAttributesLabel = tk.Label(self.frameAttributes, textvariable=self.frameAttributesText)
        self.frameAttributesLabel.pack(side=tk.TOP)

        # toolbars
        self.toolBoxDraw = ToolBox(self.frameUpper, 'Draw', self.onChange, tools=Config['Tools']['Draw'], radio=True)
        self.divider1 = tk.Label(self.frameUpper, width=2, text='|').pack(side=tk.LEFT, padx=10)
        self.toolsTransfer = ToolBox(self.frameUpper, 'Transfer', self.onChange, tools=Config['Tools']['Transfer'])
        self.divider2 = tk.Label(self.frameUpper, width=2, text='|').pack(side=tk.LEFT, padx=10)
        self.toolsMatch = ToolBox(self.frameUpper, 'Match', self.onChange, tools=Config['Tools']['Match'])
        self.divider3 = tk.Label(self.frameUpper, width=2, text='|').pack(side=tk.LEFT, padx=10)
        self.toolsPreview = ToolBox(self.frameUpper, 'Preview', self.onChange, tools=Config['Tools']['Preview'])

    def onChange(self, toolBox, tool):
        self.command(toolBox, tool)

    def setToolFromKey(self, id):
        self.toolBoxDraw.setTool(id)
        self.setTool(id)

    def setTool(self, id):
        self.currentTool = id
        self.frameAttributesText.set(id)

    def beginToolPath(self, mouse):
        self.toolPath.beginPath(mouse.x, mouse.y)

    def updateToolPath(self, mouse):
        self.toolPath.moveTo(mouse.x, mouse.y)

    def clearToolPath(self):
        self.toolPath.clearPath()
