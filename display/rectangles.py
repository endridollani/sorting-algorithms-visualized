import pygame
import time
import random
pygame.init()


class Rectangles():
    def __init__(self,number_of_rectangles):
        self.number_of_rectangles = number_of_rectangles
        self.array_of_numbers = self.initialize_new_array_of_numbers()
        self.default_color = (255,255,255)

    def set_color_to_default_value(self): self.default_color = (255,255,255) 

    def get_array_of_numbers(self): return self.array_of_numbers
   
    def get_rectangle_at(self,pos,val):
        left_p = 0
        if pos != 0:
            left_p = round(1300 / self.number_of_rectangles) * pos
        return pygame.Rect(left_p,700 - round(650 * (val + 1) / (self.number_of_rectangles + 5)), round(1300 / self.number_of_rectangles),round(650 * (val + 1) / self.number_of_rectangles))

    def draw_rectangles(self,window,swaped_colour = (255,0,0),swap1 = None,swap2 = None):

        for i in self.array_of_numbers:
            val = i
            pos = self.array_of_numbers.index(val)
            rectangle = self.get_rectangle_at(pos,val)
            
            if swap1 == pos:
                pygame.draw.rect(window,swaped_colour, rectangle)
                swap1 = None
            elif swap2 == pos:
                pygame.draw.rect(window,swaped_colour, rectangle)
                swap2 = None
            else:
                pygame.draw.rect(window,self.default_color, rectangle)
            
    def sort_finished(self,window,delay):
        for i in self.array_of_numbers:
            val = i
            pos = self.array_of_numbers.index(val)
            rectangle = self.get_rectangle_at(pos,val)

            time.sleep(delay)
            pygame.draw.rect(window,(46, 209, 54), rectangle)
            pygame.display.flip()
    
    def initialize_new_array_of_numbers(self):
        array_of_numbers = [n for n in range(self.number_of_rectangles)]
        random.shuffle(array_of_numbers)
        return array_of_numbers