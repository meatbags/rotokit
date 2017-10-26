import Tkinter as tk
from src.master import Master
from src.gui import *
from src.menu import *
from src.config import *
from src.event import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Rotokit')
        self.iconbitmap('icon.ico')

        # create menus & tools
        self.masterHandler = Master(self)
        self.menuHandler = MenuHandler(self, lambda menu, item: self.masterHandler.handleMenuItem(item))

        # keyboard events
        self.eventHandler = EventHandler(self)
        self.eventHandler.bindKeyDown(lambda event: self.masterHandler.handleKeyDown(event))
        self.eventHandler.bindKeyRelease(lambda event: self.masterHandler.handleKeyRelease(event))

        # run
        self.mainloop()
