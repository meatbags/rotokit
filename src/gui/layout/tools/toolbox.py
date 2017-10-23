import tkinter as tk
from src.gui.layout.tools.tool import Tool
from src.config import Config

class ToolBox(tk.Frame):
    def __init__(self, root, id, command, tools=[], radio=False, columns=10, **kw):
        super().__init__(root, kw)
        self.pack(side=tk.LEFT, padx=8)
        self.command = command
        self.id = id

        # populate
        self.createButtons(tools, radio, columns)

    def createButtons(self, tools, radio, columns):
        self.lastTool = tk.StringVar()
        self.tools = {key: Tool(self.id + '_Tool_' + key, key, self.onToolChange) for key in tools}

        # get buttons
        n = 0
        if radio:
            self.radioVar = tk.StringVar()
            for tool in self.tools:
                column = int(n % columns)
                row = int((n - column) / 2)
                self.tools[tool].getRadioButton(self, var=self.radioVar, row=row, column=column)
                n += 1
        else:
            for tool in self.tools:
                column = int(n % columns)
                row = int((n - column) / 2)
                self.tools[tool].getCheckButton(self, row=row, column=column)
                n += 1

    def onToolChange(self, tool):
        # pass event up
        self.command(self, tool)
