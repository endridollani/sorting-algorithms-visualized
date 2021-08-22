import pygame
import random
from pygame import time
from pygame.draw import rect


class SortingAlgorithms:
    def __init__(self,number):
        self.rect = Rectangles(number)
        self.numbers_arr = self.rect.get_num_arr()
        self.number = number
        self.sorting_state = [False, ""]
        self.rects = self.rect.get_rects(self.numbers_arr)
        self.i = 0
        self.index = 0
        self.count = 0
        self.iterations = self.number - 1
    
    def display(self,window):
        self.rect.draw_rects(window)

    def get_sort_state(self): return self.sorting_state
    def set_sort_state(self,bool,string):  self.sorting_state = [bool,string]

    def bubble_sort(self,window):
        
        if self.i < self.iterations:

            if self.numbers_arr[self.index] > self.numbers_arr[self.index + 1]:
                
                self.numbers_arr[self.index],self.numbers_arr[self.index+1] = self.numbers_arr[self.index+1], self.numbers_arr[self.index]
                self.rect.set_num_arr(self.numbers_arr)

            self.index += 1

            if self.index >= self.iterations:
                self.iterations -= 1
                self.index = 0
                self.i += 0
                self.count += 1

            print(f"index:{self.index}\ni:{self.count}")
        else:
            self.sorting_state = [False,""]
            print("bubble sort finished")
            self.timer,self.index,self.iterations,self.count,self.i = 0,0,(self.number - 1),0,0

        self.rect.draw_rects(window)
    
    def shuffle_array(self):
        self.sorting_state = [False,""]
        self.timer,self.index,self.i = 0,0,0
        self.rect.shuffle_arr()
    

class Rectangles():
    def __init__(self,number_of_rects):
        self.number_of_rects = number_of_rects
        self.numbers_arr = self.init_new_arr()
        self.rects = []
        self.shuffle_arr()

    
    def get_num_arr(self): return self.numbers_arr
    def get_rectangles(self): return self.rects
    def set_num_arr(self,arr): 
        self.numbers_arr = arr
        self.rects = self.get_rects(self.numbers_arr)
    
    
    def set_rect(self,i, r):
        self.rects[i] = r

    def draw_rects(self,window):

        for rect in self.rects:
            pygame.draw.rect(window,(53,234,56), rect)
    

    def init_new_arr(self):
        return [n for n in range(self.number_of_rects)]

    def shuffle_arr(self):
        random.shuffle(self.numbers_arr)
        self.rects = self.get_rects(self.numbers_arr) 
    
    def get_rects(self,numbers):
        rects = []
        left_p = 0
        for i in numbers:
            rects.append(pygame.Rect(left_p,700 - round(650 * (i + 1) / (len(numbers) + 5)), round(1300 / len(numbers)),round(650 * (i + 1) / len(numbers)))) 
            left_p += round(1300 / len(numbers)) 
        return rects
