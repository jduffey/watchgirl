# This is an example that uses pygame.draw.rect:
# From: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

import os, sys
import random
import pygame
from pygame.locals import *
import time
import random

pygame.init()

windowTitle = 'Identifier #580CD2E889BD - Onett Art Museum Main Entrance'

BORDER_THICKNESS = 5
NUMBER_OF_SQUARES = 4
SQUARE_WIDTH = 150
PERIOD = 1

APP_X_SIZE = NUMBER_OF_SQUARES * SQUARE_WIDTH
APP_Y_SIZE = SQUARE_WIDTH

myRed = (255, 0, 0)
myBlue = (0, 0, 255)
myGreen = (0, 255, 0)
myYellow = (255, 255, 0)
myWhite = (255, 255, 255)
myLightRed = (255, 180, 180)
myLightBLue = (190, 190, 255)
myBlack = (0, 0, 0)

squareOne = (0, 0, 1 * APP_X_SIZE/NUMBER_OF_SQUARES, APP_Y_SIZE)
squareTwo = (1 * APP_X_SIZE/NUMBER_OF_SQUARES, 0, 2 * APP_X_SIZE/NUMBER_OF_SQUARES, APP_Y_SIZE)
squareThree = (2 * APP_X_SIZE/NUMBER_OF_SQUARES, 0, 3 * APP_X_SIZE/NUMBER_OF_SQUARES, APP_Y_SIZE)
squareFour = (3 * APP_X_SIZE/NUMBER_OF_SQUARES, 0, 4 * APP_X_SIZE/NUMBER_OF_SQUARES, APP_Y_SIZE)

screen = pygame.display.set_mode((APP_X_SIZE + BORDER_THICKNESS, APP_Y_SIZE))
pygame.display.set_caption(windowTitle)
pygame.mouse.set_visible(True)
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

def drawColorSquare(whichSquare):
    pygame.draw.rect(screen, getRandomColor(), whichSquare)

def drawSquareBorders():
    pygame.draw.rect(screen, myBlack, (0, 0, BORDER_THICKNESS, APP_Y_SIZE))
    pygame.draw.rect(screen, myBlack, (1 * APP_X_SIZE/NUMBER_OF_SQUARES, 0, BORDER_THICKNESS, APP_Y_SIZE))
    pygame.draw.rect(screen, myBlack, (2 * APP_X_SIZE/NUMBER_OF_SQUARES, 0, BORDER_THICKNESS, APP_Y_SIZE))
    pygame.draw.rect(screen, myBlack, (3 * APP_X_SIZE/NUMBER_OF_SQUARES, 0, BORDER_THICKNESS, APP_Y_SIZE))

    pygame.draw.rect(screen, myBlack, (0, 0, APP_X_SIZE + BORDER_THICKNESS, BORDER_THICKNESS))
    pygame.draw.rect(screen, myBlack, (0, APP_Y_SIZE - BORDER_THICKNESS, APP_X_SIZE + BORDER_THICKNESS, BORDER_THICKNESS))
    pygame.draw.rect(screen, myBlack, (APP_X_SIZE, 0, BORDER_THICKNESS, APP_Y_SIZE))


while isDrawingActive:

    drawColorSquare(squareOne)
    drawColorSquare(squareTwo)
    drawColorSquare(squareThree)
    drawColorSquare(squareFour)

    drawSquareBorders()

    pygame.display.flip()
    time.sleep(PERIOD)

    print(time.time())
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