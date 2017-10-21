import tkinter as tk
from src.interface.gui_config import *

class ToolBar:
    def __init__(self, root):
        # tool
        self.tool = tk.StringVar()

        # create toolbar
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.TOP, fill=tk.Y)

        # populate
        for tool in Config['Toolbar']['Tools']:
            self.addButton(tool)

    def addButton(self, key):
        # add radio button to toolbar
        tk.Radiobutton(
            self.frame,
            width=Config['Toolbar']['ButtonWidth'],
            command=self.onClick,
            text=key,
            variable=self.tool,
            value=Config['Toolbar']['Tools'][key],
            indicatoron=False).pack(anchor=tk.NW)

    def onClick(self):
        pass

    def getTool(self):
        return self.tool.get()

    def getFrame(self):
        return self.frame
