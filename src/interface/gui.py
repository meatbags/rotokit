# setup the TK app

from tkinter import *
from src.interface.gui_menu import *
from src.interface.gui_layout import *
from src.interface.gui_config import *

class GUI:
    def __init__(self):
        # init gui
        self.root = Tk()
        self.root.title('Rotokit')
        self.root.geometry(Config['Root']['InitialDimensions'])

        # create menus & tools
        self.menu = MenuBar(self.root)
        self.layout = Layout(self.root)

        # run
        self.root.mainloop()
