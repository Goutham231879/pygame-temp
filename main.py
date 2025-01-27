import pygame
                         #this code creates a window of size 1280 720 until user quit a black window is generated on to the screen in which games are rendered
pygame.init()
WINDOW_WIDTH , WINDOW_HEIGHT = 1280 , 720 
DISPLAY_SURFACE= pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT));
run = True;
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;    

pygame.quit()
