import tkinter as tk
from src.master import Master
from src.gui import *
from src.config import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('')
        self.iconbitmap('icon.ico')

        # create menus & tools
        self.menu = MenuBar(self)
        self.layout = Master(self)

        # keyboard events
        self.events = Events(self)
        self.events.bindKeyDown(lambda event: self.layout.handleKeyDown(event))
        self.events.bindKeyRelease(lambda event: self.layout.handleKeyRelease(event))

        # run
        self.mainloop()
