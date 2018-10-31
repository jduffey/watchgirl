# This is an example that uses pygame.draw.rect:
# From: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

import os, sys
import random
import pygame
from pygame.locals import *
import time
import random

pygame.init()

APP_SQUARE_SIZE = 600

APP_X_SIZE = 400
APP_Y_SIZE = 100

myRed = (255, 0, 0)
myBlue = (0, 0, 255)
myGreen = (0, 255, 0)
myYellow = (255, 255, 0)
myWhite = (255, 255, 255)
myLightRed = (255, 180, 180)
myLightBLue = (190, 190, 255)

# squareOne = (0, 0, APP_SQUARE_SIZE/2, APP_SQUARE_SIZE/2)
# squareTwo = (APP_SQUARE_SIZE/2, 0, APP_SQUARE_SIZE, APP_SQUARE_SIZE/2)
# squareThree = (0, APP_SQUARE_SIZE/2, APP_SQUARE_SIZE/2, APP_SQUARE_SIZE)
# squareFour = (APP_SQUARE_SIZE/2, APP_SQUARE_SIZE/2, APP_SQUARE_SIZE, APP_SQUARE_SIZE)

squareOne = (0, 0, 1 * APP_X_SIZE/4, APP_Y_SIZE)
squareTwo = (1 * APP_X_SIZE/4, 0, 2 * APP_X_SIZE/4, APP_Y_SIZE)
squareThree = (2 * APP_X_SIZE/4, 0, 3 * APP_X_SIZE/4, APP_Y_SIZE)
squareFour = (3 * APP_X_SIZE/4, 0, 4 * APP_X_SIZE/4, APP_Y_SIZE)

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption('Identifier #580CD2E889BD - Onett Art Museum Main Entrance')
pygame.mouse.set_visible(True)
#pygame.mouse.set_visible(False)
squareThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
squareThatIsTheSizeOfTheScreen.fill((255, 255, 255))
screen.blit(squareThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

isDrawingActive = True

def getRandomColor():
    randnum = random.randint(0,3)
    if randnum == 0:
        nextColor = myRed
    if randnum == 1:
        nextColor = myBlue
    if randnum == 2:
        nextColor = myGreen
    if randnum == 3:
        nextColor = myYellow
    return nextColor


while isDrawingActive:

    pygame.draw.rect(screen, getRandomColor(), squareOne)
    pygame.draw.rect(screen, getRandomColor(), squareTwo)
    pygame.draw.rect(screen, getRandomColor(), squareThree)
    pygame.draw.rect(screen, getRandomColor(), squareFour)
    pygame.display.flip()
    time.sleep(2)
    #print(time.time())
    # squareThatIsTheSizeOfTheScreen.fill((255, 255, 255))
    # screen.blit(squareThatIsTheSizeOfTheScreen, (0, 0))
    # pygame.display.flip()
    # time.sleep(.5)
    
    
        # If you delete the below line you should no longer see the vibrant colors.
       #pygame.display.flip()
    
        # if the 'X' button is pressed the window should close:
    Geesh = pygame.event.get()
    
    if len(Geesh) > 0:
        if Geesh[0].type == QUIT: isDrawingActive = False
    ## Once this line is reached the window should close