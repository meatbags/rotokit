from src.frame.layer import Layer
import tkinter as tk
import random

class Frame:
    def __init__(self, id, canvas):
        self.id = str(id)
        self.targetCanvas = canvas

        # tk vars
        self.lastSoloVar = tk.StringVar()
        self.soloVar = tk.StringVar()

        # layers
        self.layers = []
        self.newLayer('Background')

        for i in range(random.randrange(1, 10)):
            self.newLayer(i)

    def draw(self):
        # draw layers to target canvas
        solo = self.soloVar.get()

        if solo == '':
            # draw normally
            for layer in self.layers:
                layer.draw(self.targetCanvas)
        else:
            # draw solo layer, hide others
            for layer in self.layers:
                layer.solo(solo, self.targetCanvas)

    def setCanvas(self, canvas):
        # set target canvas
        self.targetCanvas = canvas

    def newLayer(self, label):
        # add new blank layer
        id = self.id + '_layer_' + str(len(self.layers))
        self.layers.append(Layer(self, id, label))

    def onSoloLayer(self):
        # set solo layer
        if self.lastSoloVar.get() == self.soloVar.get():
            self.lastSoloVar.set('')
            self.soloVar.set('')
        else:
            self.lastSoloVar.set(self.soloVar.get())

        # redraw
        self.draw()

    def onHideLayer(self):
        # draw layers
        self.draw()

    def addLayerList(self, root):
        # add list of layers to element
        self.title = tk.Frame(root)
        self.title.pack(side=tk.TOP, fill=tk.X)
        self.titleText = tk.Label(self.title, text=self.id)
        self.titleText.pack(side=tk.LEFT)

        for i in range(len(self.layers)-1, -1, -1):
            self.layers[i].addListItem(root, self.soloVar, self.onSoloLayer, self.onHideLayer)
