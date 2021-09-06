import pygame
from pygame import font
import time

font.init()

font = pygame.font.SysFont('arial', 15)

def display_sort_algorithm_information(window, algorithm, swap_number, array_writes, number_of_rectangles, delay_in_millisecondes):
    algorithm_selected = font.render(
        f'{algorithm}', True, (255, 255, 255), (0, 0, 0))
    algorithm_rect_number = font.render(
        f'Rectangles: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    algorithm_swaps = font.render(
        f'Swaps: {swap_number}', True, (255, 255, 255), (0, 0, 0))
    algorithm_writes = font.render(
        f'Array Writes: {array_writes}', True, (255, 255, 255), (0, 0, 0))
    delays = font.render(
        f'Delay {delay_in_millisecondes * 1000} ms', True, (255, 255, 255), (0, 0, 0))

    window.blit(algorithm_selected, (10, 10))
    window.blit(algorithm_rect_number, (10, 30))
    window.blit(algorithm_swaps, (10, 50))
    window.blit(algorithm_writes, (10, 70))
    window.blit(delays, (10, 90))
