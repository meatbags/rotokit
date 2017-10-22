from src.gui.layout.canvas.layer import Layer

class Frame:
    def __init__(self, id='FRAME'):
        self.id = id
        self.layers = []
        self.layers.append(Layer(self, 'Background'))
