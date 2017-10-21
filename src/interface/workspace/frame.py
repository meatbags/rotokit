from src.interface.workspace.layer import *

class Frame:
    def __init__(self):
        self.layers = [Layer() for i in range(5)]
