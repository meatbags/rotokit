from src.interface.config import *
import pygame
import random

class Layer(pygame.Surface):
    def __init__(self, size=Config['Canvas']['DefaultSize']):
        super().__init__(size, pygame.SRCALPHA, 32)
        self.convert_alpha()
        self.stroke = (255, 0, 0)
        self.lineWidth = 1
        self.start = (random.random() * size[0], random.random() * size[1])
        self.end = (random.random() * size[0], random.random() * size[1])
        self.requiresDraw = True

    def draw(self):
        pygame.draw.line(self, self.stroke, self.start, self.end, self.lineWidth)
