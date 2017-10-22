import tkinter as tk

class LayerRow(tk.Frame):
    def __init__(self, root):
        super().__init__(root, borderwidth=4, relief=tk.SUNKEN)
        self.label = tk.Label(self, text='Layer')
        self.label.pack(side=tk.LEFT)

        self.visible = tk.IntVar()
        self.eye = tk.Checkbutton(self, variable=self.visible, text='Eye')
        self.eye.pack(side=tk.LEFT)

        self.pack(side=tk.BOTTOM)
