import tkinter as tk
from src.interface.sidebar.toolbar import *
from src.interface.layout.pane import *
from src.interface.workspace.workspace import *

class Layout(tk.PanedWindow):
    def __init__(self, root):
        # master pane
        super().__init__(root)
        self.config(orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)
        self.pack(fill=tk.BOTH, expand=1)

        # side bar
        self.sidebar = Pane(self)
        self.toolbar = ToolBar(self.sidebar)

        # main window
        self.main = Pane(self, orient=tk.VERTICAL)
        self.viewer = Pane(self.main)
        self.workspace = Workspace(self.viewer)
        self.timeline = Pane(self.main, label='TIMELINE')
