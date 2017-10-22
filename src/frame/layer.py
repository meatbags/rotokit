from src.config import Config
from src.maths import Transform
from src.frame.objects import Path
import random
import tkinter as tk

class Layer:
    def __init__(self, parent, id, name):
        self.parent = parent
        self.id = str(id)
        self.name = str(name)

        # vars
        self.requiresDraw = True
        self.hidden = tk.IntVar()
        self.locked = tk.IntVar()

        # transform
        self.transform = Transform()

        # objects
        self.objects = []
        for i in range(5):
            self.addPath()

    def draw(self, canvas):
        if self.hidden.get() == 1:
            self.hide(canvas)
        else:
            for obj in self.objects:
                obj.draw(canvas, self.id)

    def hide(self, canvas):
        canvas.delete(self.id)

        for obj in self.objects:
            obj.requiresDraw = True

    def solo(self, id, canvas):
        if id == self.id:
            self.draw(canvas)
        else:
            self.hide(canvas)

    def addPath(self):
        id = self.id + '_path_' + str(len(self.objects))
        self.objects.append(Path(self, id))

    def addListItem(self, root, selectVar=None, selectCmd=None, soloVar=None, soloCmd=None, hideCmd=None):
        item = tk.Frame(root, relief=tk.SUNKEN)
        item.pack(side=tk.TOP, fill=tk.X, expand=1)
        buttonSelect = tk.Radiobutton(item, variable=selectVar, command=selectCmd, value=self.id, text=self.name, font=Config['Global']['Font'], indicatoron=False)
        buttonSelect.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        buttonHide = tk.Checkbutton(item, variable=self.hidden, command=hideCmd, text='H', indicatoron=False)
        buttonHide.pack(side=tk.RIGHT)
        buttonSolo = tk.Radiobutton(item, variable=soloVar, value=self.id, command=soloCmd, text='S', indicatoron=False)
        buttonSolo.pack(side=tk.RIGHT)
        buttonLock = tk.Checkbutton(item, variable=self.locked, text='L', indicatoron=False)
        buttonLock.pack(side=tk.RIGHT)
