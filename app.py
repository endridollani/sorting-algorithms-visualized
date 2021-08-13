import pygame
import time
from window import window
from gui import gui
from events import handler
pygame.init()

window = window.Window((1360, 700), "Sorting Visualized")
gui, handler = gui.Gui(window.get_display_mode()), handler.EventHandler(window.get_display_mode())

if __name__ ==  "__main__":
    running = True
    clock = pygame.time.Clock()
    FPS = 60


    while(running):
        clock.tick(FPS)
        window.redraw(gui)

        for event in pygame.event.get():
            handler.handle_event(event.type)        
