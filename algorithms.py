import pygame
import random
from pygame import time

pygame.font.init()

class SortingAlgorithms:
    def __init__(self,number):
        self.rect = Rectangles(number)
        self.numbers_arr = self.rect.get_num_arr()
        self.number = number
        self.iterations = self.number - 1
        self.i,self.index,self.count = 0,0,0
        self.sorting_state = [False, ""]
        self.array_access = 0
        self.swaps = 0
        self.sw1,self.sw2 = 0,0
        self.shuffled = True
        # Font & Text
        self.font = pygame.font.SysFont('arial',15)
        self.algorithm_selected = self.font.render('Algorithm Selected: None', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_rect_number = self.font.render(f'Rectangles Drawn: {number}', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_swaps = self.font.render(f'Swaps: None', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_writes = self.font.render(f'Array Writes: None', True, (255, 255, 255), (0, 0, 0))

    def display(self,window):
        self.draw_text(window)
        self.rect.draw_rects(window)
    def is_shuffled(self): return self.shuffled 
    def draw_text(self,window):
        window.blit(self.algorithm_selected,(10,10))
        window.blit(self.algorithm_rect_number,(10,30))
        window.blit(self.algorithm_swaps,(10,50))
        window.blit(self.algorithm_writes,(10,70))
   
    def get_sort_state(self): return self.sorting_state
    
    def set_sort_state(self,bool,string):  self.sorting_state = [bool,string]

    def bubble_sort(self,window):
        if self.i < self.iterations:
            if self.numbers_arr[self.index] > self.numbers_arr[self.index + 1]:
                self.swap(self.index)
            self.index += 1
            if self.index >= self.iterations:
                self.iterations -= 1
                self.index = 0
                self.i += 0
                self.count += 1
        else:
            self.sorting_state = [False,""]
            print("bubble sort finished")
            self.index,self.iterations,self.count,self.i = 0,(self.number - 1),0,0
            print(f"There were {self.swaps} array accesses!")
            self.shuffled = False

        if not self.sorting_state[0]:
            self.render_text(swaps=self.swaps)
            self.draw_text(window)
            self.rect.draw_rects(window,finished=(53, 234, 56))
        else:
            self.render_text(swaps =self.swaps)
            self.draw_text(window)
            self.rect.draw_rects(window,sw1 = self.sw1,sw2=self.sw2)


    def render_text(self,algorithm_selected = None,swaps = None, array_writes = None):
        if algorithm_selected != None:
            self.algorithm_selected = self.font.render(f'Algorithm Selected: {algorithm_selected}', True, (255, 255, 255), (0, 0, 0))
        if swaps != None:
            self.algorithm_swaps = self.font.render(f'Swaps: {swaps}', True, (255, 255, 255), (0, 0, 0))
        if array_writes != None:
            self.algorithm_writes = self.font.render(f'Array Writes: {array_writes}', True, (255, 255, 255), (0, 0, 0))

    def render_default_text(self):
        self.algorithm_selected = self.font.render('Algorithm Selected: None', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_swaps = self.font.render(f'Swaps: None', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_writes = self.font.render(f'Array Writes: None', True, (255, 255, 255), (0, 0, 0))

    def swap(self,i):
        self.sw1,self.sw2 = i,i+1
        self.numbers_arr[i],self.numbers_arr[i+1] = self.numbers_arr[i+1],self.numbers_arr[i]
        self.swaps+=1
        self.render_text(array_writes=self.swaps * 2)

    def shuffle_array(self):
        self.sorting_state = [False,""]
        self.swaps,self.index,self.iterations,self.count,self.i = 0,0,(self.number - 1),0,0
        random.shuffle(self.numbers_arr)
        self.rect.set_default_color_to_white()
        self.render_default_text()
        self.shuffled = True


class Rectangles():
    def __init__(self,number_of_rects):
        self.number_of_rects = number_of_rects
        self.numbers_arr = self.init_new_arr()
        self.default_color = (255,255,255)

    def set_default_color_to_white(self): self.default_color = (255,255,255) 

    def get_num_arr(self): return self.numbers_arr
   
    def get_at_pos_val(self,pos,val):
        left_p = 0
        if pos != 0:
            left_p = round(1300 / self.number_of_rects) * pos
        return pygame.Rect(left_p,700 - round(650 * (val + 1) / (self.number_of_rects + 5)), round(1300 / self.number_of_rects),round(650 * (val + 1) / self.number_of_rects))

    def draw_rects(self,window,swaped_colour = (255,0,0),sw1 = None,sw2 = None,finished = None):

        for i in self.numbers_arr:
            val = i
            pos = self.numbers_arr.index(val)
            rectangle = self.get_at_pos_val(pos,val)
            if sw1 == pos:
                pygame.draw.rect(window,swaped_colour, rectangle)
                sw1 = None
            elif sw2 == pos:
                pygame.draw.rect(window,swaped_colour, rectangle)
                sw2 = None
            elif finished != None:
                pygame.draw.rect(window,finished, rectangle)
                self.default_color = finished
            else:
                pygame.draw.rect(window,self.default_color, rectangle)
    
    def init_new_arr(self):
        arr = [n for n in range(self.number_of_rects)]
        random.shuffle(arr)
        return arr