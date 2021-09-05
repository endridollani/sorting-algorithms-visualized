import pygame
from pygame.sprite import RenderUpdates
import pygame_gui

class Button:

    def __init__(self,window,width,height):
        self.window = window
        self.manager = pygame_gui.UIManager((width,height), 'visualization/display/button_theme.json')

        self.shuffle_button = self.set_button(relative_rect=pygame.Rect((255, 5), (100, 30)), text='Shuffle')

        self.bubble_sort_button = self.set_button(relative_rect=pygame.Rect((360, 5), (100, 30)),text='Bubble Sort')

        self.selection_sort_button = self.set_button(relative_rect=pygame.Rect((465, 5), (150, 30)),text='Selection Sort')
       
        self.insertion_sort_button = self.set_button(relative_rect=pygame.Rect((620, 5), (150, 30)),text='Insertion Sort')
        
        self.merge_sort_button = self.set_button(relative_rect=pygame.Rect((775, 5), (100, 30)),text='Merge Sort')

        self.quick_sort_button = self.set_button(relative_rect=pygame.Rect((880, 5), (100, 30)),text='Quick Sort')
        
        self.heap_sort_button = self.set_button(relative_rect=pygame.Rect((985, 5), (100, 30)),text='Heap Sort')
        
        self.tim_sort_button = self.set_button(relative_rect=pygame.Rect((1090, 5), (100, 30)),text='Tim Sort')
        
        self.intro_sort_button = self.set_button(relative_rect=pygame.Rect((1195, 5), (100, 30)),text='Intro Sort')

    
    def set_button(self,relative_rect,text):
        return pygame_gui.elements.UIButton(relative_rect,text,self.manager)
    
    def get_shuffle_button(self):
        return self.shuffle_button

    def get_bubble_sort_button(self):
        return self.bubble_sort_button
    
    def get_selection_sort_button(self):
        return self.selection_sort_button
    
    def get_insertion_sort_button(self):
        return self.insertion_sort_button

    def get_merge_sort_button(self):
        return self.merge_sort_button

    def get_quick_sort_button(self):
        return self.quick_sort_button

    def get_heap_sort_button(self):
        return self.heap_sort_button

    def get_tim_sort_button(self):
        return self.tim_sort_button
    
    def get_intro_sort_button(self):
        return self.intro_sort_button

    def display(self): 
        self.manager.draw_ui(self.window)

    def get_manager(self): return self.manager

    def update_delta_time(self, delta_time):
        self.manager.update(delta_time)
