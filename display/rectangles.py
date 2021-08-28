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

    def draw_rectangles(self,window,swaped_colour = (255,0,0),sw1 = None,sw2 = None,finished = None):

        for i in self.array_of_numbers:
            val = i
            pos = self.array_of_numbers.index(val)
            rectangle = self.get_rectangle_at(pos,val)
            
            if sw1 == pos:
                pygame.draw.rect(window,swaped_colour, rectangle)
                sw1 = None
            elif sw2 == pos:
                pygame.draw.rect(window,swaped_colour, rectangle)
                sw2 = None
            elif finished != None:
                time.wait(50)
                pygame.draw.rect(window,finished, rectangle)
                pygame.display.flip()
                self.default_color = finished
            else:
                pygame.draw.rect(window,self.default_color, rectangle)
    
    def initialize_new_array_of_numbers(self):
        array_of_numbers = [n for n in range(self.number_of_rectangles)]
        random.shuffle(array_of_numbers)
        return array_of_numbers