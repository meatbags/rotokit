import Tkinter as tk
from src.tools.tool import Tool
from src.config import Config

class ToolBox(tk.Frame):
    def __init__(self, root, id, command, tools={}, radio=False, columns=10, **kw):
        tk.Frame.__init__(self, root, kw)
        self.pack(side=tk.LEFT)
        self.id = str(id)

        # commands
        self.command = command

        # vars
        self.radioVar = tk.StringVar()

        # populate
        self.createButtons(tools, radio, columns)

    def createButtons(self, tools, radio, columns):
        self.lastTool = tk.StringVar()
        self.tools = {key: Tool(tools[key], key, self.onToolChange) for key in tools}

        # get buttons
        n = 0
        if radio:
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

    def setTool(self, id):
        self.radioVar.set(id)

    def onToolChange(self, tool):
        # pass event up
        self.command(self, tool)
