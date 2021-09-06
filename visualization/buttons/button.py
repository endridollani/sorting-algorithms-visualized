import pygame
import pygame_gui

BUTTONS = {}

#Initializes buttons
def init_buttons(manager):
    BUTTONS['SHUFFLE'] = set(relative_rect=pygame.Rect((255, 5), (100, 30)), text='Shuffle',manager=manager)
    BUTTONS['BUBBLE_SORT'] = set(relative_rect=pygame.Rect((360, 5), (100, 30)),text='Bubble Sort',manager=manager)
    BUTTONS['SELECTION_SORT'] = set(relative_rect=pygame.Rect((465, 5), (150, 30)),text='Selection Sort',manager=manager)
    BUTTONS['INSERTION_SORT'] = set(relative_rect=pygame.Rect((620, 5), (150, 30)),text='Insertion Sort',manager=manager)
    BUTTONS['MERGE_SORT'] = set(relative_rect=pygame.Rect((775, 5), (100, 30)),text='Merge Sor',manager=manager)
    BUTTONS['QUICK_SORT'] = set(relative_rect=pygame.Rect((880, 5), (100, 30)),text='Quick Sort',manager=manager)
    BUTTONS['HEAP_SORT'] = set(relative_rect=pygame.Rect((985, 5), (100, 30)),text='Heap Sort',manager=manager)
    BUTTONS['TIM_SORT'] = set(relative_rect=pygame.Rect((1090, 5), (100, 30)),text='TimSort',manager=manager)
    BUTTONS['INTRO_SORT'] = set(relative_rect=pygame.Rect((1195, 5), (100, 30)),text='IntroSort',manager=manager)


def set(relative_rect,text,manager):
    return pygame_gui.elements.UIButton(relative_rect,text,manager)

def get(type):
    return BUTTONS.get(type)