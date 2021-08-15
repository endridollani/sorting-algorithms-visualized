import pygame
import time
import window
import gui
import handler
pygame.init()

if __name__ ==  "__main__":
    window = window.Window()
    gui = gui.Gui()
    handler = handler.EventHandler()

    running = True
    clock = pygame.time.Clock()
    FPS = 60

    while(running):
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            handler.handle_event(event)

        gui.update_delta_time(time_delta)

        window.redraw(gui)
