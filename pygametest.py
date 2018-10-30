# This is an example that uses pygame.draw.rect:
# From: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

import os, sys
import random
import pygame
from pygame.locals import *

pygame.init()
APP_X_SIZE = 400
APP_Y_SIZE = 400

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption('Fun Boring Example comes with Source Code too!!')
pygame.mouse.set_visible(True)
#pygame.mouse.set_visible(False)
squareThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
squareThatIsTheSizeOfTheScreen.fill((255, 255, 255))
screen.blit(squareThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

isDrawingActive = True
while isDrawingActive:
    # a color can be: (0 to 255, 0 to 255, 0 to 255)
   myRed = (255, 0, 0)
   myBlue = (0, 0, 255)
   myGreen = (0, 255, 0)
   myYellow = (255, 255, 0)
   myWhite = (255, 255, 255)
   myLightRed = (255, 180, 180)
   myLightBLue = (190, 190, 255)
   topLeft = (0, 0, 200, 200)
   topRight = (200, 0, 400, 200)
   bottomLeft = (0, 200, 200, 400)
   bottomRight = (200, 200, 400, 400)
    # "screen.set_at((x, y), Color)" and "pygame.draw.rect(screen, Color, (x, y, x_size, y_size))" draw colors on to an "in computer memory image" called: "screen"
   # screen.set_at(( 1,  1), myYellow)
   # screen.set_at(( 2,  2), myYellow)
   # screen.set_at(( 3,  3), myYellow)
   # screen.set_at(( 4,  4), myYellow)
   # screen.set_at(( 5,  5), myYellow)
   # screen.set_at(( 6,  6), myYellow)
   # screen.set_at(( 7,  7), myYellow)
   # screen.set_at(( 8,  8), myYellow)
   # screen.set_at(( 9,  9), myYellow)
   # screen.set_at((10, 10), myYellow)
   # screen.set_at((11, 11), myYellow)
   # screen.set_at((12, 12), myYellow)
   # screen.set_at((13, 13), myYellow)
   # screen.set_at((14, 14), myYellow)
   # screen.set_at((15, 15), myYellow)
   # screen.set_at((16, 16), myYellow)
   # screen.set_at((17, 17), myYellow)
   # screen.set_at((18, 18), myYellow)
   # screen.set_at((19, 19), myYellow)
   # screen.set_at((20, 20), myYellow)
   pygame.draw.rect(screen, myRed, topLeft)
   pygame.draw.rect(screen, myBlue, topRight)
   pygame.draw.rect(screen, myGreen, bottomLeft)
   pygame.draw.rect(screen, myYellow, bottomRight)
   # pygame.draw.rect(screen, myGreen,      (200, 10,   40,   40))
   # pygame.draw.rect(screen, myLightRed,  (10,  200,  50,   50))
   # pygame.draw.rect(screen, myLightBLue, (200, 200,  60,   60))
   # pygame.draw.rect(screen, myLightBLue, (100, 200,  10,    2))
   # pygame.draw.rect(screen, myWhite,  (0, 100,  50,   52))
    # If you delete the below line you should no longer see the vibrant colors.
   pygame.display.flip()
    # if the 'X' button is pressed the window should close:
   Geesh = pygame.event.get()
   if len(Geesh) > 0:
    if Geesh[0].type == QUIT: isDrawingActive = False
## Once this line is reached the window should close