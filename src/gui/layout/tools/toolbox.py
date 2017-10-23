import tkinter as tk
from src.gui.layout.tools.tool import Tool
from src.config import Config

class ToolBox(tk.Frame):
    def __init__(self, root, tools=[], radio=False, onChange=None, columns=10, **kw):
        super().__init__(root, kw)
        self.pack()

        # populate
        self.lastTool = tk.StringVar()
        self.tools = {
            key: Tool(key, key) for key in tools
        }

        # get buttons
        n = 0

        if radio:
            self.radioVar = tk.StringVar()
            for tool in self.tools:
                column = int(n % columns)
                row = int((n - column) / 2)
                self.tools[tool].getRadioButton(self, var=self.radioVar, cmd=self.onTool, row=row, column=column)
                n += 1
        else:
            for tool in self.tools:
                column = int(n % columns)
                row = int((n - column) / 2)
                self.tools[tool].getCheckButton(self, cmd=self.onTool, row=row, column=column)
                n += 1

    def onTool(self):
        print('Clicked')
