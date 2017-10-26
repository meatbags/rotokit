import aggdraw
from PIL import Image
import Tkinter as tk

class Renderer:
    def __init__(self, size):
        self.size = size
        self.centre = (size[0]/2, size[1]/2)
        self.pen = aggdraw.Pen('black')

    def clear(self, canvas):
        canvas.delete('all')

    def render(self, canvas, frame):
        for layer in frame.layers:
            if layer.hidden:
                self.hideLayer(canvas, layer)
            else:
                self.renderLayer(canvas, layer)

    def hideLayer(self, canvas, layer):
        canvas.delete(layer.id)

    def renderLayer(self, canvas, layer):
        if layer.requiresDraw:
            # delete pre-existing layer images
            canvas.delete(layer.id)

            # create a new PIL image and draw objects
            layer.clearImage()
            image = Image.new('RGBA', self.size)
            draw = aggdraw.Draw(image)

            for path in layer.paths:
                for obj in path.objects:
                    draw.line((obj.p1.x, obj.p1.y, obj.p2.x, obj.p2.y), self.pen)

            # pass PIL image to ImageTk.PhotoImage and place on canvas
            draw.flush()
            layer.image.paste(image)
            canvas.create_image(self.centre, image=layer.image, tags=layer.id)

            # flag as drawn
            layer.requiresDraw = False
        elif not canvas.find_withtag(layer.id):
            # display last drawn image
            canvas.create_image(self.centre, image=layer.image, tags=layer.id)

            # flag as shown
            layer.requiresShow = False
