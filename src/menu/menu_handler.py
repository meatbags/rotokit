import Tkinter as tk
from src.menu.menu import Menu
from src.config import Config

class MenuHandler(tk.Menu):
    def __init__(self, root, command):
        tk.Menu.__init__(self, root)
        self.command = command

        # add menus
        for key in Config['Menu']:
            newMenu = Menu(self, key, self.onMenuChange)
            self.add(itemType='cascade', label=key, menu=newMenu)

        # pack
        root.config(menu=self)

    def onMenuChange(self, menu, item):
        self.command(menu, item)
