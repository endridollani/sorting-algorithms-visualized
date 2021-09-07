import pygame
from pygame import display
import pygame_gui
from buttons import button


def get_user_input():
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
    
    return (array_size,delay_in_millisecondes)

class Handler():
    def __init__(self,manager):
        self.manager = manager
        self.algorithm_display = None
    
    def set_display_link(self,algorithm_display):
        self.algorithm_display = algorithm_display

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
                        self.algorithm_display.shuffle_array()
                    if event.ui_element == button.get('BUBBLE_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(0)

                    if event.ui_element == button.get('SELECTION_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(1)
                   
                    if event.ui_element == button.get('INSERTION_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(2)

                    if event.ui_element == button.get('MERGE_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(3)

                    if event.ui_element == button.get('QUICK_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(4)

                    if event.ui_element == button.get('HEAP_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(5)
                    
                    if event.ui_element == button.get('TIM_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(6)

                    if event.ui_element == button.get('INTRO_SORT'):
                        self.algorithm_display.set_index_of_algorithm_chosen(7)

            self.manager.process_events(event)