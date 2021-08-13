import pygame

class Window:
   
    def __init__(self):
        self.window = pygame.display.set_mode((1300, 700), pygame.SCALED)
        self.caption = pygame.display.set_caption("Visualized Sorting")  

    def display_set_dimensions(self,dimensions): self.window = self.display_set_mode(dimensions=dimensions)

    def display_set_mode(self, dimensions): return pygame.display.set_mode(dimensions, pygame.SCALED)

    def get_win(self): return self.window

    def redraw(self, gui):
        gui.display(self.window)
        pygame.display.update()