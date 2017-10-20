import tkinter as tk
#import src.interface.gui_menu as gui_menu
#import src.interface.gui_tool as gui_tool

class Pane:
    def __init__(self, root, orient=tk.HORIZONTAL, label=False):
        self.pane = tk.PanedWindow(root, orient=orient, sashwidth=6, sashrelief=tk.SUNKEN)
        if label:
            self.pane.add(tk.Label(text=label))
        root.add(self.pane)

class Layout:
    def __init__(self, root):
        # layout panes
        self.master = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)
        self.master.pack(fill=tk.BOTH, expand=1)
        self.sidebar = Pane(self.master, label='SIDE BAR')
        self.main = Pane(self.master, orient=tk.VERTICAL)
        self.viewer = Pane(self.main.pane)
        self.timeline = Pane(self.main.pane, label='TIMELINE')
        self.left = Pane(self.viewer.pane, label='LEFT')
        self.right = Pane(self.viewer.pane, label='RIGHT')

        # sidebar -> layers & toolbar
        # timeline -> timeline & more tools
        # viewer right, left -> canvas
