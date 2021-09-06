import pygame
import pygame_gui
import draw
from buttons import button

class EventHandler():
    def __init__(self,manager):
        self.manager = manager
    
    # def set_algorithm_to_check(self,algorithm): self.algorithm = algorithm

    def check_for_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
        
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    if event.ui_element == button.get('SHUFFLE'):
                        self.algorithm.shuffle_array()

                    if event.ui_element == button.get('BUBBLE_SORT'):
                        draw.SORT_INDEX = 0

                    if event.ui_element == button.get('SELECTION_SORT'):
                        draw.SORT_INDEX = 1
                   
                    if event.ui_element == button.get('INSERTION_SORT'):
                        draw.SORT_INDEX = 2

                    if event.ui_element == button.get('MERGE_SORT'):
                        draw.SORT_INDEX = 3

                    if event.ui_element == button.get('QUICK_SORT'):
                        draw.SORT_INDEX = 4

                    if event.ui_element == button.get('HEAP_SORT'):
                        draw.SORT_INDEX = 5
                    
                    if event.ui_element == button.get('TIM_SORT'):
                        draw.SORT_INDEX = 6

                    if event.ui_element == button.get('INTRO_SORT'):
                        draw.SORT_INDEX = 7

            self.manager.process_events(event)
            