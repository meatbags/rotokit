import tkinter as tk
from src.interface.menu.menu import *
from src.interface.layout.layout import *
from src.interface.config import *

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rotokit')
        self.geometry(Config['Root']['InitialDimensions'])

        # create menus & tools
        self.menu = MenuBar(self)
        self.layout = Layout(self)

        # run
        self.mainloop()
