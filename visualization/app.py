import pygame
import time
import draw
from window import Window
import event_handler

pygame.init()
ARRAY_SIZE,DELAY = event_handler.get_user_input()


if __name__ ==  "__main__":
    running = True
    clock = pygame.time.Clock()
    FPS = 60
            
    window = Window()
    handler = event_handler.Handler(window.get_manager())
    draw_to_window = draw.Draw(window,ARRAY_SIZE,DELAY)

    #Links the event occurred with the draw.py class wich has the logic behind that event.
    handler.set_button_event_logic_handler(draw_to_window)
     
    while(running):
        time_delta = clock.tick(FPS) / 1000.0
        handler.check_for_events(pygame.event.get())
        window.update_gui_manager(time_delta)
        window.set_background() 
        window.display_buttons()

        if draw_to_window.is_required_for_sorting:
            draw_to_window.sort_visualization()
        else:
            draw_to_window.rectangle_bar_chart()

        pygame.display.flip()

