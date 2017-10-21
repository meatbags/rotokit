import tkinter as tk
import pygame
import os
from src.interface.config import *
from src.interface.workspace.canvas import *
from src.interface.workspace.frame import *
from src.interface.workspace.camera import *

class Workspace(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.conf = Config['Workspace']

        self.size = self.conf['DefaultSize']
        self.config(width=self.size[0], height=self.size[1])
        self.pack(fill=tk.BOTH)

        # embed
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        # pygame setup
        self.display = pygame.display.set_mode(self.size)
        self.display.fill(self.conf['BackgroundColour'])

        # set up
        self.camera = Camera()
        self.canvasLeft = Canvas(position=(0, 0))
        self.canvasRight = Canvas(position=(Config['Canvas']['DefaultSize'][0] + self.conf['CanvasSeparation'], 0))
        self.frameLeft = Frame()
        self.frameRight = Frame()

        # run
        self.draw()
        root.add(self)

    def draw(self):
        self.display.fill(self.conf['BackgroundColour'])
        self.canvasLeft.draw(self.frameLeft, self.camera)
        self.canvasRight.draw(self.frameRight, self.camera)
        self.display.blit(self.canvasLeft, self.canvasLeft.position)
        self.display.blit(self.canvasRight, self.canvasRight.position)

        # pygame update
        pygame.display.update()
