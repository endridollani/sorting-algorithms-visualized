import pygame
import time
import draw
from window import Window
import event_handler

ARRAY_SIZE,DELAY = event_handler.get_user_input()

pygame.init()

if __name__ ==  "__main__":
    running = True
    clock = pygame.time.Clock()
    FPS = 60
            
    window = Window()
    handler = event_handler.Handler(window.get_manager())
    display = draw.Draw(window,ARRAY_SIZE,DELAY)
    
    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        handler.check_for_events(pygame.event.get())
        window.update_gui_manager(time_delta)
        window.set_background() 
        window.display_buttons()

        if display.sort_state:
            # display.rectangle_visualization()
            print('ss')
        else:
            # display.rectangles()
            print("sss")

        pygame.display.flip()

