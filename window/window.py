import pygame

class Window:

    def __init__(self, dimensions, caption):
        self.window = self.set_display_mode(dimensions)
        self.caption = self.set_caption(caption)

    def set_caption(self, caption):
        return pygame.display.set_caption(caption)

    def set_display_mode(self,dimensions):
        return pygame.display.set_mode(dimensions, pygame.SCALED)

    def get_display_mode(self):
        return self.window
    
    def redraw(self, gui):
        pass