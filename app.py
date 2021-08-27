from typing import Text
import pygame
import time
import window
import gui
import handler
import algorithms
pygame.init()

# while True:
#     try:
#         number_of_rectangles = abs(int(input("Set the number of items you want to be sorted: ")))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

number_of_rectangles = 65

if __name__ ==  "__main__":
    window = window.Window()
    gui = gui.Gui()
    algorithm = algorithms.SortingAlgorithms(number_of_rectangles)
    handler = handler.EventHandler(algorithm)

    running = True
    clock = pygame.time.Clock()
    FPS = 60

    def check_for_events():
        for event in pygame.event.get():
            handler.handle_event(event)

    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        check_for_events()
        gui.update_delta_time(time_delta)
        window.set_bg()
        gui.display(window.get_win())

        
        if(algorithm.get_sort_state() == [True,"bubble_sort"]):
            algorithm.render_text("Bubble Sort")
            if not algorithm.is_shuffled():
                algorithm.set_sort_state(False,"")
                algorithm.display(window.get_win())

            else:
                for i in range(number_of_rectangles):
                    # time_delta = clock.tick(FPS) / 1000.0
                    # check_for_events()
                    # update_gui_and_window(time_delta)
                    for j in range(number_of_rectangles - 1):
                       

                        index1 = algorithm.rect.get_num_arr()[j]
                        index2 = algorithm.rect.get_num_arr()[j+1]
                        if index1 > index2:

                            time.sleep(0.0001)
                            algorithm.swap(j)
                        
                        window.set_bg()
                        algorithm.rect.draw_rects(window=window.get_win())
                        pygame.display.flip()
                algorithm.set_sort_state(False,"")
                algorithm.rect.draw_rects(window.get_win(),finished=(53, 234, 56))
        else:
            algorithm.display(window.get_win())

        
        pygame.display.flip()
