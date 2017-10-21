from src.interface.config import *
import pygame

class Canvas(pygame.Surface):
    def __init__(self, position=(0, 0), size=Config['Canvas']['DefaultSize']):
        super().__init__(size)

        self.position = position
        self.fill(Config['Canvas']['BackgroundColour'])

    def draw(self, frame, camera):
        self.fill(Config['Canvas']['BackgroundColour'])

        for layer in frame.layers:
            if layer.requiresDraw:
                layer.draw()
            self.blit(layer, (0, 0))
