from src.config import Config
from src.menu.menu_item import MenuItem
import Tkinter as tk

class Menu(tk.Menu):
    def __init__(self, root, id, command, **kw):
        tk.Menu.__init__(self, root, tearoff=0, **kw)
        self.id = str(id)
        self.command = command

        # add items
        for item in Config['Menu'][id]:
            newItem = MenuItem(self, item, self.onMenuChange)

    def onMenuChange(self, item):
        self.command(self.id, item)
