import pygame
import pygame_gui
from gui import Gui

class EventHandler(Gui):
    def __init__(self,algorithm):
        super().__init__()
        self.manager = super().get_manager()
        self.shuffle_btn = super().get_shuffle_btn()
        self.merge_sort_btn = super().get_merge_sort_btn()
        self.quick_sort_btn = super().get_quick_sort_btn()
        self.heap_sort_btn = super().get_heap_sort_btn()
        self.bubble_sort_btn = super().get_bubble_sort_btn()
        # self.sort_btn = super().get_sort_btn()
        self.algorithm = algorithm

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
    
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.shuffle_btn:
                    self.algorithm.shuffle_array(),
                    print('Shuffled')
                if event.ui_element == self.merge_sort_btn:
                    print('merge_sort')
                if event.ui_element == self.quick_sort_btn:
                    print('quick_sort')
                if event.ui_element == self.heap_sort_btn:
                    print('heap_sort')
                if event.ui_element == self.bubble_sort_btn:
                    self.algorithm.bubble_sort()
                    print('bubble_sort')
                # if event.ui_element == self.sort_btn:
                #     print('Sort')

        self.manager.process_events(event)
        