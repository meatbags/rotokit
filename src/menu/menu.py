from tkinter import *
from src.interface.config import *

class MenuBar:
    def __init__(self, root):
        self.menuBar = Menu(root)

        for item in Config['Menu']:
            newMenu = Menu(self.menuBar, tearoff=0)

            for subitem in Config['Menu'][item]:
                newMenu.add_command(label=subitem, command=self.nullCommand)

            self.menuBar.add_cascade(label=item, menu=newMenu)

        root.config(menu=self.menuBar)

    def nullCommand(self):
        pass
