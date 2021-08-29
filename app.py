import pygame
import time
from window import Window
from handler import EventHandler
from algorithm import Algorithm
pygame.init()

while True:
    try:
        array_size = (int)(input("Enter array size: "))
        if array_size < 3:
            print("Please enter a positive number >= 3 for a better visualization")
        elif array_size>1000:
            print("Please enter a number <= 1000.")
        else:
            break
    except ValueError:
        print("Value Error! Enter an number:")

while True:
    try:
        delay_in_millisecondes = (float)(input("Enter delay in milliseconds: "))
        if (delay_in_millisecondes <= -1):
            print("Delay can't be a negative value")
        else:
            break
    except ValueError:
        print("Value Error! Enter an number:")
        
window = Window()
handler = EventHandler()
algorithm = Algorithm(array_size,delay_in_millisecondes)
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

