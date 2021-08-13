import pygame

class Gui:
    def __init__(self, window):
        self.window = window

    def display(self):
        self.window.blit((255,0,0))
        pygame.display.update()