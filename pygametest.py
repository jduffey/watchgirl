# This is an example that uses pygame.draw.rect:
# From: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

import os, sys
import random
import pygame
from pygame.locals import *
import time
import random

pygame.init()
APP_X_SIZE = 400
APP_Y_SIZE = 400

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

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption('Fun Boring Example comes with Source Code too!!')
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

    pygame.draw.rect(screen, getRandomColor(), topLeft)
    pygame.draw.rect(screen, getRandomColor(), topRight)
    pygame.draw.rect(screen, getRandomColor(), bottomLeft)
    pygame.draw.rect(screen, getRandomColor(), bottomRight)
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