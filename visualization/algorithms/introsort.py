from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

class IntroSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.swaps = 0
        self.array_accesses = 0
    
    def sort(self):
        self.introsort(super().get_array_of_numbers())
        super().draw() 
        super().draw_finishline()

    def introsort(self,alist):
        maxdepth = (len(alist).bit_length() - 1)*2
        self.introsort_helper(alist, 0, len(alist), maxdepth)
    
    def introsort_helper(self,alist, start, end, maxdepth):
        if end - start <= 1:
            return
        elif maxdepth == 0:
            self.heapsort(alist, start, end)
        else:
            p = self.partition(alist, start, end)
            self.introsort_helper(alist, start, p + 1, maxdepth - 1)
            self.introsort_helper(alist, p + 1, end, maxdepth - 1)
    
    def partition(self,alist, start, end):
        pivot = alist[start]
        i = start - 1
        j = end
        self.array_accesses += 1
        while True:
            i = i + 1
            while alist[i] < pivot:
                i = i + 1
                self.array_accesses += 1
                time.sleep(self.delay)
                self.draw(start, end, pivot,-1,-1)

            j = j - 1
            while alist[j] > pivot:
                j = j - 1
                self.array_accesses += 1
                time.sleep(self.delay)
                self.draw(start, end, pivot,-1,-1)

    
            if i >= j:
                time.sleep(self.delay)
                self.draw(start, end, pivot,-1,-1)
                return j
    
            self.swap(alist, i, j)
    
    def swap(self,alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]
        self.array_accesses += 2
        self.swaps += 1
    
    def heapsort(self,alist, start, end):
        self.build_max_heap(alist, start, end)
        for i in range(end - 1, start, -1):
            self.swap(alist, start, i)
            self.max_heapify(alist, index=0, start=start, end=i)
    
    def build_max_heap(self,alist, start, end):
        def parent(i):
            return (i - 1)//2
        length = end - start
        index = parent(length - 1)
        while index >= 0:
            self.max_heapify(alist, index, start, end)
            index = index - 1
    
    def max_heapify(self,alist, index, start, end):
        def left(i):
            return 2*i + 1
        def right(i):
            return 2*i + 2
    
        size = end - start
        l = left(index)
        r = right(index)
        if (l < size and alist[start + l] > alist[start + index]):
            largest = l
            self.array_accesses += 1
            time.sleep(self.delay)
            self.draw(-1,-1,-1,-1,-1,index,largest)
        else:
            largest = index
            time.sleep(self.delay)
            self.draw(-1,-1,-1,-1,-1,index,largest)

        if (r < size and alist[start + r] > alist[start + largest]):
            largest = r
            self.array_accesses += 1
            time.sleep(self.delay)
            self.draw(-1,-1,-1,-1,-1,index,largest)

        if largest != index:
            self.swap(alist, start + largest, start + index)
            self.max_heapify(alist, largest, start, end)
            self.array_accesses += 1
            time.sleep(self.delay)
            self.draw(-1,-1,-1,-1,-1,index,largest)


    def set_defaults(self):
        self.swaps = 0
        self.array_accesses = 0
   
    def get_array_of_numbers(self):
        return super().get_array_of_numbers()
    
    def draw(self,start,end,pivot_index,index, largest):
        self.window.set_background()
        
        self.information()
        
        for i in self.array_of_numbers:
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            
            if pos == start or pos == end:
                pygame.draw.rect(self.window.get_display(),(255, 0, 0), rectangle)
            elif pos == index or pos == largest:
                pygame.draw.rect(self.window.get_display(),(0,15,255), rectangle)
            elif pos == pivot_index:
                pygame.draw.rect(self.window.get_display(),(0,255,255), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)

        pygame.display.flip()

    def information(self):
        algorithm = font.render(
            "Intro Sort", True, (255, 255, 255), (0, 0, 0))
        rectangles_drawn = font.render(
            f'Rectangles: {len(super().get_array_of_numbers())}', True, (255, 255, 255), (0, 0, 0))
        swaps = font.render(
            f'Swaps: {self.swaps}', True, (255, 255, 255), (0, 0, 0))
        array_accesses = font.render(
            f'Array Accesses: {self.array_accesses}', True, (255, 255, 255), (0, 0, 0))
        delays = font.render(
            f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

        self.window.get_display().blit(algorithm, (10, 10))
        self.window.get_display().blit(rectangles_drawn, (10, 30))
        self.window.get_display().blit(swaps, (10, 50))
        self.window.get_display().blit(array_accesses, (10, 70))
        self.window.get_display().blit(delays, (10, 90))
