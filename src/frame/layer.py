from src.config import Config
from src.maths import Transform, Vector
from src.frame.path import Path
from src.frame.path_objects import BezierCurve
import random
import Tkinter as tk
from PIL import ImageTk, Image
from random import random

class Layer:
    def __init__(self, parent, id, name, size):
        self.parent = parent
        self.id = str(id)
        self.name = str(name)
        self.size = size
        self.input = None
        self.output = None

        # vars
        self.hiddenVar = tk.IntVar()
        self.lockedVar = tk.IntVar()
        self.hidden = False
        self.requiresDraw = True
        self.requiresPartialDraw = False

        # transform
        self.transform = Transform()

        # paths
        self.paths = []

        for i in range(3):
            p = Path(self.uid('path'))
            p.addObject(
                BezierCurve(
                    Vector(random() * 100, random() * 100),
                    Vector(random() * 100, random() * 100),
                    Vector(random() * 100, random() * 100),
                    Vector(random() * 100, random() * 100)
                )
            )
            self.addPath(p)

    def addPath(self, path):
        self.paths.append(path)

    def uid(self, prefix):
        if hasattr(self, 'counter'):
            self.counter += 1
        else:
            self.counter = 0

        uid = self.id + '_' + prefix + '_' + str(self.counter)

        return uid

    def clearInput(self):
        self.input = Image.new('RGBA', self.size)

    def clearOutput(self):
        self.output = ImageTk.PhotoImage('RGBA', self.size)

    def clear(self):
        self.paths = []
        self.requiresDraw = True

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
