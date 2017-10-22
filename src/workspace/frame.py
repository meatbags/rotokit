from src.interface.workspace.layer import *

class Frame:
    def __init__(self, id='FRAME'):
        self.id = id
        self.layers = []
        self.layers.append(Layer(self, 'Background'))
