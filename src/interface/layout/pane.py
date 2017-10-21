import tkinter as tk

class Pane(tk.PanedWindow):
    def __init__(self, root, orient=tk.HORIZONTAL, label=False):
        super().__init__(root, orient=orient, sashwidth=6, sashrelief=tk.SUNKEN)

        # add placeholder label
        if label:
            self.add(tk.Label(text=label))

        # add to parent
        root.add(self)
