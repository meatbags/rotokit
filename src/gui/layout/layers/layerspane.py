import tkinter as tk

class LayersPane(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(side=tk.TOP)

        self.left = tk.Frame(self, width=120)
        self.left.pack(side=tk.LEFT, fill=tk.Y)
        self.separator = tk.Frame(self, width=10)
        self.separator.pack(side=tk.LEFT, fill=tk.Y)
        self.right = tk.Frame(self, width=80)
        self.right.pack(side=tk.LEFT, fill=tk.Y)

        root.add(self)
