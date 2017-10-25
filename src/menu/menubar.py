import tkinter as tk
from src.config import Config

class MenuItem:
    def __init__(self, root, label, command):
        self.id = Config['Menu'][root.id][label]['ID']
        self.shortcut = Config['Menu'][root.id][label]['Shortcut']
        self.command = command
        root.add(
            itemType='command',
            label=label,
            accelerator=self.shortcut,
            command=self.onMenuChange
        )

    def onMenuChange(self):
        self.command(self.id)


class Menu(tk.Menu):
    def __init__(self, root, id, command, **kw):
        super().__init__(root, tearoff=0, **kw)
        self.id = str(id)
        self.command = command

        # add items
        for item in Config['Menu'][id]:
            newItem = MenuItem(self, item, self.onMenuChange)

    def onMenuChange(self, item):
        self.command(self.id, item)


class MenuBar(tk.Menu):
    def __init__(self, root, command):
        super().__init__(root)
        self.command = command

        # add menus
        for key in Config['Menu']:
            newMenu = Menu(self, key, self.onMenuChange)
            self.add(itemType='cascade', label=key, menu=newMenu)

        # pack
        root.config(menu=self)

    def onMenuChange(self, menu, item):
        self.command(menu, item)
