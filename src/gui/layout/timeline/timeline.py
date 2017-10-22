import tkinter as tk

class Timeline(tk.PanedWindow):
    def __init__(self, root):
        super().__init__(root, orient=tk.HORIZONTAL, sashwidth=6, sashrelief=tk.SUNKEN)
        self.add(tk.Label(text='The Timeline'))
        root.add(self)
