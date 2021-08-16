import pygame
import time
import window
import gui
import handler
import algorithms
pygame.init()

if __name__ ==  "__main__":
    window = window.Window()
    gui = gui.Gui()
    algorithm = algorithms.SortingAlgorithms(100)
    handler = handler.EventHandler(algorithm)

    running = True
    clock = pygame.time.Clock()
    FPS = 60

    while(running):
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            handler.handle_event(event)

        gui.update_delta_time(time_delta)

        window.redraw(gui,algorithm)
