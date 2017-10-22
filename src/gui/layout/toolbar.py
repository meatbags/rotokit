import tkinter as tk
from src.config import Config

class ToolBar(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(side=tk.TOP, fill=tk.Y)

        # tool
        self.tool = tk.StringVar()

        # populate toolbar
        for tool in Config['Toolbar']['Tools']:
            self.addButton(tool)

        root.add(self)

    def addButton(self, key):
        # add radio button to toolbar
        tk.Radiobutton(
            self,
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
