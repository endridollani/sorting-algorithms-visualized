import pygame
import time
from window import window
from gui import gui
from events import handler
pygame.init()

window = window.Window()
gui, handler = gui.Gui(), handler.EventHandler()

if __name__ ==  "__main__":
    running = True
    clock = pygame.time.Clock()
    FPS = 60

    while(running):
        clock.tick(FPS)
        window.redraw(gui)

        for event in pygame.event.get():
            handler.handle_event(event.type)        
