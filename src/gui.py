import tkinter as tk
from src.interface.menu.menu import *
from src.interface.layout.layout import *
from src.interface.events.events import *
from src.interface.config import *

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rotokit')

        # create menus & tools
        self.menu = MenuBar(self)
        self.layout = Layout(self)

        # events
        self.events = Events(self)

        # run
        self.mainloop()

    def onEvent(self, event):
        print(event)
