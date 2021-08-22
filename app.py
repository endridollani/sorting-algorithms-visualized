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
    algorithm = algorithms.SortingAlgorithms(50)
    handler = handler.EventHandler(algorithm)

    running = True
    clock = pygame.time.Clock()
    FPS = 100

    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            handler.handle_event(event)

        gui.update_delta_time(time_delta)
        window.set_bg()
        gui.display(window.get_win())
        
        if(algorithm.get_sort_state() == [True,"bubble_sort"]):
            algorithm.bubble_sort(window.get_win())
        else:
            algorithm.display(window.get_win())

        
        pygame.display.flip()
