import tkinter as tk
from src.gui.menu import MenuBar
from src.master import Master
from src.gui.event import Events
from src.config import Config

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('')
        self.iconbitmap('icon.ico')

        # create menus & tools
        self.menu = MenuBar(self)
        self.layout = Master(self)

        # events
        self.events = Events(self)

        # run
        self.mainloop()

    def onEvent(self, event):
        print(event)
