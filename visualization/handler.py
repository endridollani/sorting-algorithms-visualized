import pygame
import pygame_gui
from window import Window

class EventHandler(Window):
    def __init__(self):
        super().__init__()
        self.button = super().get_button()
        self.manager = self.button.get_manager()
        self.shuffle_btn = self.button.get_shuffle_button()
        self.merge_sort_btn = self.button.get_merge_sort_button()
        self.quick_sort_btn = self.button.get_quick_sort_button()
        self.heap_sort_btn = self.button.get_heap_sort_button()
        self.bubble_sort_btn = self.button.get_bubble_sort_button()

        self.algorithm = None

    def set_algorithm_to_check(self,algorithm): self.algorithm = algorithm

    def check_for_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
        
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.shuffle_btn:
                        self.algorithm.shuffle_array()
                    if event.ui_element == self.merge_sort_btn:
                        self.algorithm.set_index_of_algorithm_chosen(index=0)
                    if event.ui_element == self.quick_sort_btn:
                        self.algorithm.set_index_of_algorithm_chosen(index=1)
                    if event.ui_element == self.heap_sort_btn:
                        self.algorithm.set_index_of_algorithm_chosen(index=2)
                    if event.ui_element == self.bubble_sort_btn:
                        self.algorithm.set_index_of_algorithm_chosen(index=3)

            self.manager.process_events(event)
            