import Tkinter as tk

class Pane(tk.PanedWindow):
    def __init__(self, root, label=None, **kw):
        tk.PanedWindow.__init__(self, root, kw, sashpad=8, sashwidth=2, sashrelief=tk.SUNKEN)

        # add placeholder label
        if label:
            self.add(tk.Label(text=label))

        # add to parent
        root.add(self)
