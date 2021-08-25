from typing import Text
import pygame
import time
import window
import gui
import handler
import algorithms
pygame.init()

while True:
    try:
        number_of_rectangles = abs(int(input("Set the number of items you want to be sorted: ")))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


if __name__ ==  "__main__":
    window = window.Window()
    gui = gui.Gui()
    algorithm = algorithms.SortingAlgorithms(number_of_rectangles)
    handler = handler.EventHandler(algorithm)

    running = True
    clock = pygame.time.Clock()
    FPS = 60

    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            handler.handle_event(event)

        gui.update_delta_time(time_delta)
        window.set_bg()
        gui.display(window.get_win())
        
        if(algorithm.get_sort_state() == [True,"bubble_sort"]):
            algorithm.render_text("Bubble Sort")
            if not algorithm.is_shuffled():
                algorithm.set_sort_state(False,"")
                algorithm.display(window.get_win())

            else:
                algorithm.bubble_sort(window.get_win())
        else:
            algorithm.display(window.get_win())

        
        pygame.display.flip()
