from tkinter import *
from src.interface.gui_config import *

class MenuBar:
    def __init__(self, master):
        self.menuBar = Menu(master)

        for item in Config['Menu']:
            newMenu = Menu(self.menuBar, tearoff=0)

            for subitem in Config['Menu'][item]:
                newMenu.add_command(label=subitem, command=self.nullCommand)

            self.menuBar.add_cascade(label=item, menu=newMenu)

        master.config(menu=self.menuBar)

    def nullCommand(self):
        pass
