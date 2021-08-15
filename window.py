import pygame

class Window:
   
    def __init__(self):
        self.window = pygame.display.set_mode((1300, 700), pygame.SCALED)
        self.caption = pygame.display.set_caption("Visualized Sorting")
        self.background = pygame.Surface((1300, 700))
        self.background.fill(pygame.Color('#000000')) 

    def display_set_dimensions(self,dimensions): self.window = self.display_set_mode(dimensions=dimensions)

    def display_set_mode(self, dimensions): return pygame.display.set_mode(dimensions, pygame.SCALED)

    def get_window_dimensions(self): return (1300, 700)

    def redraw(self, gui):
        self.window.blit(self.background, (0, 0))
        gui.display(self.window)
        
        pygame.display.update()