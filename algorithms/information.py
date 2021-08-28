from pygame import font    

def display_sort_algorithm_information(window,algorithm,swap_number,array_writes,number_of_rectangles):
    algorithm_selected = font.render(f'Algorithm Selected: {algorithm}', True, (255, 255, 255), (0, 0, 0))
    algorithm_rect_number = font.render(f'Rectangles Drawn: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    algorithm_swaps = font.render(f'Swaps: {swap_number}', True, (255, 255, 255), (0, 0, 0))
    algorithm_writes = font.render(f'Array Writes: {array_writes}', True, (255, 255, 255), (0, 0, 0))
    
    window.blit(algorithm_selected,(10,10))
    window.blit(algorithm_rect_number,(10,30))
    window.blit(algorithm_swaps,(10,50))
    window.blit(algorithm_writes,(10,70))