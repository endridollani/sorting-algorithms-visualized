import pygame
import pygame_gui
from gui import Gui

class EventHandler(Gui):
    def __init__(self):
        super().__init__()
        self.manager = super().get_manager()
        self.shuffle_btn = super().get_shuffle_btn()
        self.array_size_btn = super().get_array_size_btn()
        self.algorithm_picker_btn = super().get_algorithm_picker_btn()
        self.sort_btn = super().get_sort_btn()
    
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()
        
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.shuffle_btn:
                    print('Shuffle')
                if event.ui_element == self.array_size_btn:
                    print('Pick Array Size')
                if event.ui_element == self.algorithm_picker_btn:
                    print('Pick Sortin Algorithm')
                if event.ui_element == self.sort_btn:
                    print('Sort')
        
        self.manager.process_events(event)
        