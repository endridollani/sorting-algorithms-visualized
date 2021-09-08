import pygame
import time
import random
# from pygame import font

# font.init()
pygame.init()

# font = pygame.font.SysFont('arial', 15)

class Rectangles:
    def __init__(self,window,number_of_rectangles,delay):
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.array_of_numbers = self.initialize_new_array_of_numbers()

    def get_array_of_numbers(self): return self.array_of_numbers
    def set_array_of_numbers(self,array): self.array_of_numbers = array
    def get_rectangle_at(self,pos,val):
        left_p = (1300 / self.number_of_rectangles) * pos
        return pygame.Rect(left_p,700 - (650 * (val + 1) / (self.number_of_rectangles + 5)), (1300 / self.number_of_rectangles),(650 * (val + 1) / self.number_of_rectangles))

    def draw(self):
        # self.information()
        
        for i in self.array_of_numbers:
            val = i
            pos = self.array_of_numbers.index(val)
            rectangle = self.get_rectangle_at(pos,val)
            
            pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)
        
    def draw_finishline(self):
        for i in self.array_of_numbers:
            val = i
            pos = self.array_of_numbers.index(val)
            rectangle = self.get_rectangle_at(pos,val)

            time.sleep(self.delay)
            pygame.draw.rect(self.window.get_display(),(0, 255, 0), rectangle)
            pygame.display.flip()
        
    
    # def information(self):
    #     rectangle_number = font.render(
    #         f'Rectangles: {self.number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    #     delays = font.render(
    #         f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

    #     self.window.get_display().blit(rectangle_number, (10, 10))
    #     self.window.get_display().blit(delays, (10, 30))
       
    # def draw_quick_sort(self,window,start,end,pivot):
    #     for i in self.array_of_numbers:
    #         val = i
    #         pos = self.array_of_numbers.index(val)
    #         rectangle = self.get_rectangle_at(pos,val)
            
    #         if pos == start or pos == end:
    #             pygame.draw.rect(window,(255, 0, 0), rectangle)
    #         elif pos == pivot:
    #             pygame.draw.rect(window,(0,255,255), rectangle)
    #         else:
    #             pygame.draw.rect(window,(255,255,255), rectangle)
    
    # def draw_heap_sort(self,window,index, largest):
    #     for i in self.array_of_numbers:
    #         val = i
    #         pos = self.array_of_numbers.index(val)
    #         rectangle = self.get_rectangle_at(pos,val)
    #         if pos == index or pos == largest:
    #             pygame.draw.rect(window,(0,15,255), rectangle)
    #         else:
    #             pygame.draw.rect(window,(255,255,255), rectangle)

    # def draw_merge_sort(self,window,l,r,m,li,ri):
    #     for i in self.array_of_numbers:
    #         val = i
    #         pos = self.array_of_numbers.index(val)
    #         rectangle = self.get_rectangle_at(pos,val)
    #         if pos == l or pos == r:
    #             pygame.draw.rect(window.get_display(),(0, 255, 0), rectangle)
    #         elif pos == m:
    #             pygame.draw.rect(window.get_display(),(0, 150, 255), rectangle)
    #         elif pos == li or pos == ri:
    #             pygame.draw.rect(window.get_display(),(255, 0, 0), rectangle)
    #         else:
    #             pygame.draw.rect(window.get_display(),(255, 255, 255), rectangle)

    # def draw_bubble_sort(self,window,swap_index):

    #     for i in self.array_of_numbers:
    #         val = i
    #         pos = self.array_of_numbers.index(val)
    #         rectangle = self.get_rectangle_at(pos,val)
            

    #         if pos == swap_index or pos == swap_index+1:
    #             pygame.draw.rect(window,(255,0,0), rectangle)
            
    #         else:
    #             pygame.draw.rect(window,(255,255,255), rectangle)
                
            
    # def sort_finished(self,window,delay):
    #     for i in self.array_of_numbers:
    #         val = i
    #         pos = self.array_of_numbers.index(val)
    #         rectangle = self.get_rectangle_at(pos,val)

    #         time.sleep(delay)
    #         pygame.draw.rect(window,(0, 255, 0), rectangle)
    #         pygame.display.flip()
    
    def initialize_new_array_of_numbers(self):
        array_of_numbers = [n for n in range(self.number_of_rectangles)]
        random.shuffle(array_of_numbers)
        return array_of_numbers