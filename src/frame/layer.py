from src.config import Config
from src.maths import Transform
from src.frame.frame_objects import Path
import random
import Tkinter as tk
from PIL import ImageTk

class Layer:
    def __init__(self, parent, id, name, size):
        self.parent = parent
        self.id = str(id)
        self.name = str(name)
        self.size = size
        self.image = ImageTk.PhotoImage('RGBA', self.size)

        # vars
        self.hiddenVar = tk.IntVar()
        self.lockedVar = tk.IntVar()
        self.requiresDraw = True
        self.hidden = False

        # transform
        self.transform = Transform()

        # paths
        self.paths = []

        for i in range(5):
            self.addPath()

    def clearImage(self):
        self.image = ImageTk.PhotoImage('RGBA', self.size)

    def addPath(self):
        id = self.id + '_path_' + str(len(self.paths))
        self.paths.append(Path(self, id))

    def addListItem(self, root, selectVar=None, selectCmd=None, soloVar=None, soloCmd=None, hideCmd=None):
        # container
        item = tk.Frame(root, relief=tk.SUNKEN)
        item.pack(side=tk.TOP, fill=tk.X, expand=1)

        # hide
        def onHide():
            self.hidden = (self.hiddenVar.get() == 1)
            hideCmd(self)

        # buttons
        buttonSelect = tk.Radiobutton(item, variable=selectVar, command=lambda:selectCmd(self), value=self.id, text=self.name, font=Config['Global']['Font'], indicatoron=False)
        buttonSelect.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        buttonHide = tk.Checkbutton(item, variable=self.hiddenVar, command=onHide, text='H', indicatoron=False)
        buttonHide.pack(side=tk.RIGHT)
        buttonSolo = tk.Radiobutton(item, variable=soloVar, command=lambda:soloCmd(self), value=self.id, text='S', indicatoron=False)
        buttonSolo.pack(side=tk.RIGHT)
        buttonLock = tk.Checkbutton(item, variable=self.lockedVar, text='L', indicatoron=False)
        buttonLock.pack(side=tk.RIGHT)
