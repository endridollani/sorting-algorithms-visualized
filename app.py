import pygame
import time
from window import Window
from handler import EventHandler
from algorithm import Algorithm
pygame.init()

while True:
    try:
        number_of_rectangles = (int)(input("Enter number of rectangles: "))
        break
    except ValueError:
        print("Enter an integer:")
        
window = Window()
handler = EventHandler()
algorithm = Algorithm(number_of_rectangles)
handler.set_algorithm_to_check(algorithm)

if __name__ ==  "__main__":
    running = True
    clock = pygame.time.Clock()
    FPS = 60

    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        handler.check_for_events(pygame.event.get())
        window.update_manager(time_delta)
        window.set_bg()
        window.display_buttons()

        if algorithm.is_choosen():
            algorithm.visualize(window)
        else:
            algorithm.display_shuffled_array()

        pygame.display.flip()

