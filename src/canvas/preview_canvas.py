import Tkinter as tk
from src.config import Config
from src.canvas.canvas_renderer import CanvasRenderer
from PIL import ImageTk

class PreviewCanvas(tk.Canvas):
    def __init__(self, root, id, **kw):
        tk.Canvas.__init__(self, root, kw)
        self.id = str(id)
        self.size = Config['PreviewCanvas']['DefaultSize']
        self.config(width=self.size[0], height=self.size[1], bg=Config['Canvas']['BackgroundColour'])
        self.pack(side=tk.LEFT, padx=2, pady=2)

        # image references
        self.images = []
        
        # renderer
        self.renderer = CanvasRenderer(self.size)

    def clear(self):
        self.renderer.clear(self)

    def draw(self, frames):
        # clear references
        self.images = []

        # render frames to images and place on canvas
        for frame in frames:
            self.delete(frame.id)
            self.images.append(ImageTk.PhotoImage('RGBA', self.size))
            self.renderer.renderFrameToImage(frame, self.images[-1])
            self.create_image(self.renderer.centre, image=self.images[-1], tags=frame.id)
