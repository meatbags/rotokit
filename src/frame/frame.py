from src.frame.layer import Layer
import tkinter as tk
import random

class Frame:
    def __init__(self, id):
        self.id = str(id)

        # vars
        self.lastSelectedLayerVar = tk.StringVar()
        self.selectedLayerVar = tk.StringVar()
        self.lastSoloVar = tk.StringVar()
        self.soloVar = tk.StringVar()
        self.active = False

        # layers
        self.layers = []
        self.newLayer('Background')

        for i in range(random.randrange(1, 10)):
            self.newLayer('L' + str(i))

    def draw(self, canvas):
        solo = self.soloVar.get()

        if solo == '':
            for layer in self.layers:
                layer.draw(canvas)
        else:
            for layer in self.layers:
                if layer.id == solo:
                    layer.draw(canvas)
                else:
                    layer.hide(canvas)

    def newLayer(self, label):
        # add new blank layer
        id = self.id + '_layer_' + str(len(self.layers))
        self.layers.append(Layer(self, id, label))

    def setSoloLayer(self):
        # set solo layer
        if self.lastSoloVar.get() == self.soloVar.get():
            self.lastSoloVar.set('')
            self.soloVar.set('')
        else:
            self.lastSoloVar.set(self.soloVar.get())

    def setSelectedLayer(self):
        # set selected layer
        if self.lastSelectedLayerVar.get() == self.selectedLayerVar.get():
            self.lastSelectedLayerVar.set('')
            self.selectedLayerVar.set('')
        else:
            self.lastSelectedLayerVar.set(self.selectedLayerVar.get())

    def addListItems(self, root, onChange):
        # methods
        self.onSoloLayer = lambda layer: (self.setSoloLayer(), onChange(self, layer))
        self.onHideLayer = lambda layer: (onChange(self, layer))
        self.onSelectLayer = lambda layer: (self.setSelectedLayer())

        # add list of layers to element
        title = tk.Frame(root, borderwidth=4, relief=tk.SUNKEN)
        title.pack(side=tk.TOP, fill=tk.X)
        titleText = tk.Label(title, text=self.id)
        titleText.pack(side=tk.LEFT)

        # add layer list
        layerList = tk.Frame(root)
        layerList.pack(side=tk.TOP)

        for i in range(len(self.layers)-1, -1, -1):
            self.layers[i].addListItem(
                layerList,
                selectVar=self.selectedLayerVar,
                soloVar=self.soloVar,
                selectCmd=self.onSelectLayer,
                soloCmd=self.onSoloLayer,
                hideCmd=self.onHideLayer
            )

    def resetDraw(self):
        for layer in self.layers:
            layer.resetDraw()

    def activate(self):
        self.active = True

    def disable(self):
        self.active = False
