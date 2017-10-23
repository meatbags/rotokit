import tkinter as tk
from src.config import Config

class Timeline(tk.PanedWindow):
    def __init__(self, root):
        super().__init__(root, orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)

        # toolbar
        self.toolbar = tk.Frame(self)
        self.toolbar.pack(fill=tk.X, expand=1)
        self.toolbarInnerLeft = tk.Frame(self.toolbar)
        self.toolbarInnerLeft.pack(side=tk.LEFT, fill=tk.X, expand=1)
        self.toolbarInnerRight = tk.Frame(self.toolbar)
        self.toolbarInnerRight.pack(side=tk.LEFT, fill=tk.X, expand=1)

        # tool variables
        self.tools = {
            'Transfer': {
                key: False for key in Config['Tools']['Transfer']
            },
            'Match': {
                key: False for key in Config['Tools']['Match']
            }
        }

        # populate
        for tool in Config['Tools']['Transfer']:
            t = tk.Checkbutton(self.toolbarInnerLeft, variable=self.tools['Transfer'][tool], width=10, text=tool, indicatoron=0)
            t.pack(side=tk.LEFT)

        for tool in Config['Tools']['Match']:
            t = tk.Checkbutton(self.toolbarInnerRight, variable=self.tools['Match'][tool], width=10, text=tool, indicatoron=0)
            t.pack(side=tk.LEFT)

        self.scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.pack(fill=tk.X, expand=1)

        self.timeline = tk.Label(self, text='frames, bake view')
        self.timeline.pack(fill=tk.X, expand=1)

        root.add(self)
