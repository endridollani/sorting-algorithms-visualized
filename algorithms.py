import pygame
import random
from pygame.draw import rect


class SortingAlgorithms:
    def __init__(self,number):
        self.rect = Rectangles(number)
        self.numbers_arr = []

    def display(self,window):
        self.rect.draw_rects(window)

    def bubble_sort(self):
        self.numbers_arr = self.rect.get_num_arr()
        for i in range(len(self.numbers_arr)):	#	We go through the list as many times as there are elements	
            for j in range(len(self.numbers_arr) - 1):	#	We want the pair (n-2 , n-1)
                if self.numbers_arr[j] > self.numbers_arr[j+1]:
                    self.numbers_arr[j], self.numbers_arr[j+1] = self.numbers_arr[j+1], self.numbers_arr[j]	#	Swap

        self.rect.set_num_arr(self.numbers_arr)
        
    def shuffle_array(self):
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
            rects.append((left_p,700 - round(650 * (i + 1) / (len(numbers) + 5)), round(1300 / len(numbers)),round(650 * (i + 1) / len(numbers)))) 
            left_p += round(1300 / len(numbers)) 
        return rects
