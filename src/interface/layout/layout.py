import tkinter as tk
from src.interface.sidebar.toolbar import *
from src.interface.layout.pane import *
from src.interface.workspace.workspace import *
from src.interface.workspace.timeline import *

class Layout(tk.PanedWindow):
    def __init__(self, root):
        # master pane
        super().__init__(root)
        self.config(orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)

        # side bar
        self.sidebar = Pane(self)
        self.toolbar = ToolBar(self.sidebar)

        # main window
        self.main = Pane(self, orient=tk.VERTICAL)
        self.viewer = Pane(self.main)
        self.timeline = Timeline(self.main)
        self.workspace = Workspace(self.viewer)

        # events
        self.bind('<Button-1>', self.onClick)
        #frame.bind("<Key>", key)
        #frame.bind("<Button-1>", callback)

        # pack
        self.pack(fill=tk.BOTH, expand=1)

    def onClick(self, event):
        print(event)
