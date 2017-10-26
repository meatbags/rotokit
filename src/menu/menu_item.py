import Tkinter as tk
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
