import tkinter as tk

class LayerFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # pack self
        self.pack(side=tk.TOP)
        root.add(self)

        # left and right frame
        self.left = tk.Frame(self, width=200)
        self.left.pack(side=tk.LEFT, fill=tk.Y)
        self.right = tk.Frame(self, width=200, padx=8)
        self.right.pack(side=tk.LEFT, fill=tk.Y)
