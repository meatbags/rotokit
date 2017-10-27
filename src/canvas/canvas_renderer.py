import aggdraw
import Tkinter as tk

class CanvasRenderer:
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
        if layer.requiresDraw or layer.requiresPartialDraw:
            # delete pre-existing layer images
            canvas.delete(layer.id)

            # create a new PIL image and draw objects
            layer.clearOutput()
            if not layer.requiresPartialDraw:
                layer.clearInput()

            # set input to layer image buffer
            draw = aggdraw.Draw(layer.input)

            for path in layer.paths:
                start = path.drawFrom
                stop = len(path.objects)
                for i in range(start, stop, 1):
                    obj = path.objects[i]
                    draw.line((obj.p1.x, obj.p1.y, obj.p2.x, obj.p2.y), self.pen)
                path.drawFrom = stop

            # pass PIL image to ImageTk.PhotoImage and place on canvas
            draw.flush()
            layer.output.paste(layer.input)
            canvas.create_image(self.centre, image=layer.output, tags=layer.id)

            # flag as drawn
            layer.requiresDraw = layer.requiresPartialDraw = False
        elif not canvas.find_withtag(layer.id):
            # display last drawn image
            canvas.create_image(self.centre, image=layer.output, tags=layer.id)

            # flag as shown
            layer.requiresShow = False
