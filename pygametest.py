import pygame
from pygame.locals import *
import time
import random


windowTitle = 'Identifier #580CD2E889BD - Onett Art Museum Main Entrance'

BORDER_THICKNESS = 5
SQUARE_WIDTH = 100
PERIOD_IN_SECONDS = 1

NUMBER_OF_COLUMNS = 8
NUMBER_OF_ROWS = 8

APP_X_SIZE = NUMBER_OF_COLUMNS * SQUARE_WIDTH
APP_Y_SIZE = NUMBER_OF_ROWS * SQUARE_WIDTH

myRed = (255, 0, 0)
myOrange = (255, 127, 0)
myYellow = (255, 255, 0)
myGreen = (0, 255, 0)
myBlue = (0, 0, 255)
myViolet = (75, 0, 130)
myBrown = (102, 51, 0)
myGrey = (31, 31, 31)

myBlack = (0, 0, 0)
myWhite = (255, 255, 255)


def getRandomColor():
    randnum = random.randint(0,7)
    if randnum == 0:
        nextColor = myRed
    if randnum == 1:
        nextColor = myOrange
    if randnum == 2:
        nextColor = myYellow
    if randnum == 3:
        nextColor = myGreen
    if randnum == 4:
        nextColor = myBlue
    if randnum == 5:
        nextColor = myViolet
    if randnum == 6:
        nextColor = myBrown
    if randnum == 7:
        nextColor = myGrey
    return nextColor

def drawHorizontalBorders():
    pygame.draw.rect(screen, myBlack, (0, 0, APP_X_SIZE + BORDER_THICKNESS, BORDER_THICKNESS))
    for i in range(1, NUMBER_OF_ROWS + 1):
        pygame.draw.rect(screen, myBlack, (0, i * SQUARE_WIDTH - BORDER_THICKNESS, APP_X_SIZE + BORDER_THICKNESS, BORDER_THICKNESS))

def drawVerticalBorders():
    for i in range(0, NUMBER_OF_COLUMNS + 1):
        pygame.draw.rect(screen, myBlack, (i * APP_X_SIZE/NUMBER_OF_COLUMNS, 0, BORDER_THICKNESS, APP_Y_SIZE))

def drawColorSquare(whichSquareInCurrentRow, whichRow):
    pygame.draw.rect(screen, getRandomColor(), (whichSquareInCurrentRow * APP_X_SIZE/NUMBER_OF_COLUMNS, whichRow * APP_Y_SIZE / NUMBER_OF_ROWS, (whichSquareInCurrentRow + 1) * APP_X_SIZE/NUMBER_OF_COLUMNS, (whichRow + 1) * APP_Y_SIZE / NUMBER_OF_ROWS))

screen = pygame.display.set_mode((APP_X_SIZE + BORDER_THICKNESS, APP_Y_SIZE))
pygame.display.set_caption(windowTitle)
pygame.mouse.set_visible(True)
squareThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
squareThatIsTheSizeOfTheScreen.fill((255, 255, 255))
screen.blit(squareThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

pygame.init()
isDrawingActive = True

while isDrawingActive:

    for whichRow in range(0, NUMBER_OF_ROWS):    
        for whichSquareInCurrentRow in range(0, NUMBER_OF_COLUMNS):
            drawColorSquare(whichSquareInCurrentRow, whichRow)

    drawHorizontalBorders()
    drawVerticalBorders()

    print(time.time())

    pygame.display.flip()

    # if the 'X' button is pressed the window should close:
    Geesh = pygame.event.get()
    if len(Geesh) > 0:
        if Geesh[0].type == QUIT: isDrawingActive = False

    time.sleep(PERIOD_IN_SECONDS)