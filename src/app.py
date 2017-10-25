import tkinter as tk
from src.master import Master
from src.gui import *
from src.menu import *
from src.config import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('')
        self.iconbitmap('icon.ico')

        # create menus & tools
        self._master = Master(self)
        self._menu = MenuBar(self, lambda menu, item: self._master.handleMenuItem(item))

        # keyboard events
        self._events = Events(self)
        self._events.bindKeyDown(lambda event: self._master.handleKeyDown(event))
        self._events.bindKeyRelease(lambda event: self._master.handleKeyRelease(event))

        # run
        self.mainloop()
