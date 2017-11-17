from src.frame.layer import Layer
import Tkinter as tk

class Frame:
    def __init__(self, id, size):
        self.id = str(id)
        self.size = size

        # vars
        self.lastSelectedLayerVar = tk.StringVar()
        self.selectedLayerVar = tk.StringVar()
        self.lastSoloVar = tk.StringVar()
        self.soloVar = tk.StringVar()
        self.soloMode = False
        self.soloLayer = None

        # layers
        self.activeLayer = None
        self.layers = []
        self.newLayer('Background')

        for i in range(2):
            self.newLayer('L' + str(i))

    def newLayer(self, label):
        # add new blank layer
        id = self.id + '_layer_' + str(len(self.layers))
        self.layers.append(Layer(self, id, label, self.size))

    def getLayerById(self, id):
        for layer in self.layers:
            if layer.id == id:
                return layer

        return None

    def parseToolPath(self, toolPath):
        if self.activeLayer:
            self.activeLayer.parseToolPath(toolPath)

    def setSoloLayer(self):
        # set solo layer
        if self.lastSoloVar.get() == self.soloVar.get():
            self.lastSoloVar.set('')
            self.soloVar.set('')
            self.soloMode = False
        else:
            self.lastSoloVar.set(self.soloVar.get())
            self.soloMode = True
            self.soloLayer = self.getLayerById(self.soloVar.get())

    def setSelectedLayer(self):
        # set selected layer
        if self.lastSelectedLayerVar.get() == self.selectedLayerVar.get():
            self.lastSelectedLayerVar.set('')
            self.selectedLayerVar.set('')
            self.activeLayer = None
        else:
            self.lastSelectedLayerVar.set(self.selectedLayerVar.get())
            self.activeLayer = self.getLayerById(self.selectedLayerVar.get())
            print('active', self.activeLayer.id);

    def selectDefaultLayer(self):
        if len(self.layers) > 0 and self.selectedLayerVar.get() == '':
            self.selectedLayerVar.set(self.layers[0].id)
            self.setSelectedLayer()

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
