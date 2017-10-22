from src.frame.layer import Layer
import tkinter as tk
import random

class Frame:
    def __init__(self, id):
        self.id = str(id)
        self.layers = []
        self.newLayer('Background')
        for i in range(random.randrange(1, 10)):
            self.newLayer(i)

    def newLayer(self, name):
        id = self.id + '_layer_' + str(len(self.layers))
        self.layers.append(Layer(self, id, name))

    def addButtons(self, root):
        self.title = tk.Frame(root)
        self.title.pack(side=tk.TOP, fill=tk.X)
        self.titleText = tk.Label(self.title, text=self.id)
        self.titleText.pack(side=tk.LEFT)

        for i in range(len(self.layers)-1, -1, -1):
            self.layers[i].addButton(root)
