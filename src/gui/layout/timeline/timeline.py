import tkinter as tk

class Timeline(tk.PanedWindow):
    def __init__(self, root):
        super().__init__(root, orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)
        self.scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.pack(fill=tk.X, expand=1)
        root.add(self)
