import tkinter as tk
from src.config import Config

class ToolBar(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(side=tk.TOP, fill=tk.Y)
        self.conf = Config['Toolbar']

        # tool
        self.tool = tk.StringVar()

        # populate toolbar
        self.tools = [tool for tool in self.conf['Tools']]

        for i in range(len(self.tools)):
            column = int(i % 3)
            row = int((i - column) / 3)
            self.addButton(self.tools[i], row, column)

        root.add(self)

    def addButton(self, key, row, column):
        # add radio button to toolbar
        tk.Radiobutton(
            self,
            width=Config['Toolbar']['ButtonWidth'],
            command=self.onClick,
            text=key,
            variable=self.tool,
            value=Config['Toolbar']['Tools'][key],
            indicatoron=False).grid(row=row, column=column)

    def onClick(self):
        pass

    def getTool(self):
        return self.tool.get()
