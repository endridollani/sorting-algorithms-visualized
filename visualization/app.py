import pygame
import time

from pygame import display
import draw

from window import Window
from event_handler import EventHandler

pygame.init()

if __name__ ==  "__main__":
    running = True
    clock = pygame.time.Clock()
    FPS = 60
    
    #Gets array size and checks if is a valid input 
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

    #Gets time delay and checks if is a valid input 

    while True:
        try:
            delay_in_millisecondes = (float)(input("Enter delay in milliseconds: "))
            if (delay_in_millisecondes <= -1):
                print("Delay can't be a negative value")
            else:
                break
        except ValueError:
            print("Value Error! Enter an number:")
            
    window = Window(1300,700)
    handler = EventHandler(window.get_manager())
    display = draw.Draw(window,array_size,delay_in_millisecondes)
    
    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        handler.check_for_events(pygame.event.get())
        window.update_gui_manager(time_delta)
        window.set_background() 
        window.display_buttons()

        if draw.IS_REQUIRED_FOR_SORTING:
            # display.rectangle_visualization()
            print('ss')
        else:
            # display.rectangles()
            print("sss")

        pygame.display.flip()

