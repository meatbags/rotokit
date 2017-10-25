import tkinter as tk

class LayerList(tk.Frame):
    def __init__(self, root, onChange):
        super().__init__(root, borderwidth=4, relief=tk.SUNKEN)
        self.pack(side=tk.TOP, fill=tk.BOTH)
        self.onChange = lambda frame, layer: onChange(frame, layer)

        # lists and separators
        self.elements = []

    def setActiveFrames(self, frames):
        for elem in self.elements:
            elem.destroy()

        self.elements = []

        for i in range(len(frames)):
            layerList = tk.Frame(self, borderwidth=4, relief=tk.SUNKEN)
            layerList.pack(side=tk.LEFT, fill=tk.Y)
            frames[i].addListItems(layerList, self.onChange)
            separator = tk.Frame(self, width=10)
            separator.pack(side=tk.LEFT, fill=tk.Y)

            # record
            self.elements.extend([layerList, separator])
