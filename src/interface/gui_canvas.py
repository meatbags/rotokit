from tkinter import *
from src.interface.gui_config import *

class Canvas:
    def __init__(self, master):
        self.canvas = Canvas(self, width=Config.Canvas.width, height=Config.Canvas.height)
        self.canvas.pack(side=RIGHT)
