from tkinter import *
from src.interface.gui_config import *

class ToolBar:
    def __init__(self, master):
        self.toolBar = Frame(master);
        self.toolBar.pack(side=TOP, fill=X)
        self.label = Label(self.toolBar, text='toolbar')
        self.label.grid(row=0, column=0, sticky=NW, pady=2, padx=2)
        col = 1

        for tool in Config['Toolbar']:
            toolButton = Radiobutton(self.toolBar, text=tool)
            toolButton.grid(padx=2, pady=2, row=0, column=col, sticky=NW)
            col += 1
        
