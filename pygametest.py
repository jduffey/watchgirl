import pygame
from pygame.locals import *
import time
import random
import jedhash

SECRET = "PRIVATE_KEY_GOES_HERE"
PERIOD_IN_SECONDS = 3

WINDOW_TITLE = 'Identifier #580CD2E889BD - Onett Art Museum Main Entrance'

BORDER_THICKNESS = 5
SQUARE_WIDTH = 100

NUMBER_OF_COLUMNS = 12
NUMBER_OF_ROWS = 8

APP_X_SIZE = NUMBER_OF_COLUMNS * SQUARE_WIDTH
APP_Y_SIZE = NUMBER_OF_ROWS * SQUARE_WIDTH

MY_RED = (255, 0, 0)
MY_ORANGE = (255, 127, 0)
MY_YELLOW = (255, 255, 0)
MY_GREEN = (0, 255, 0)
MY_BLUE = (0, 0, 255)
MY_VIOLET = (75, 0, 130)
MY_BROWN = (102, 51, 0)
MY_GREY = (40, 40, 40)

MY_BLACK = (0, 0, 0)
MY_WHITE = (255, 255, 255)


def getColor(currentDigest, whichSquareInCurrentRow, whichRow):
    digitToAssess = currentDigest[whichSquareInCurrentRow]
    if digitToAssess == '0' or digitToAssess == '8':
        nextColor = MY_RED
    if digitToAssess == '1' or digitToAssess == '9':
        nextColor = MY_ORANGE
    if digitToAssess == '2' or digitToAssess == 'a':
        nextColor = MY_YELLOW
    if digitToAssess == '3' or digitToAssess == 'b':
        nextColor = MY_GREEN
    if digitToAssess == '4' or digitToAssess == 'c':
        nextColor = MY_BLUE
    if digitToAssess == '5' or digitToAssess == 'd':
        nextColor = MY_VIOLET
    if digitToAssess == '6' or digitToAssess == 'e':
        nextColor = MY_BROWN
    if digitToAssess == '7' or digitToAssess == 'f':
        nextColor = MY_GREY
    return nextColor

def drawHorizontalBorders():
    pygame.draw.rect(screen, MY_BLACK, (0, 0, APP_X_SIZE + BORDER_THICKNESS, BORDER_THICKNESS))
    for i in range(1, NUMBER_OF_ROWS + 1):
        pygame.draw.rect(screen, MY_BLACK, (0, i * SQUARE_WIDTH - BORDER_THICKNESS, APP_X_SIZE + BORDER_THICKNESS, BORDER_THICKNESS))

def drawVerticalBorders():
    for i in range(0, NUMBER_OF_COLUMNS + 1):
        pygame.draw.rect(screen, MY_BLACK, (i * APP_X_SIZE/NUMBER_OF_COLUMNS, 0, BORDER_THICKNESS, APP_Y_SIZE))

def drawColorSquare(whichSquareInCurrentRow, whichRow, currentDigest):
    pygame.draw.rect(screen, getColor(currentDigest, whichSquareInCurrentRow, whichRow), (whichSquareInCurrentRow * APP_X_SIZE/NUMBER_OF_COLUMNS, whichRow * APP_Y_SIZE / NUMBER_OF_ROWS, (whichSquareInCurrentRow + 1) * APP_X_SIZE/NUMBER_OF_COLUMNS, (whichRow + 1) * APP_Y_SIZE / NUMBER_OF_ROWS))

def generateDigestForCurrentTime(whichSquareInCurrentRow):
    return jedhash.returnTheHash(SECRET, PERIOD_IN_SECONDS, whichSquareInCurrentRow)

screen = pygame.display.set_mode((APP_X_SIZE + BORDER_THICKNESS, APP_Y_SIZE))
pygame.display.set_caption(WINDOW_TITLE)
pygame.mouse.set_visible(True)
squareThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
squareThatIsTheSizeOfTheScreen.fill(MY_WHITE)
screen.blit(squareThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

pygame.init()
isDrawingActive = True

while isDrawingActive:

    for whichRow in range(0, NUMBER_OF_ROWS):
        offset = whichRow * PERIOD_IN_SECONDS
        currentDigest = generateDigestForCurrentTime(offset)
        for whichSquareInCurrentRow in range(0, NUMBER_OF_COLUMNS):
            drawColorSquare(whichSquareInCurrentRow, whichRow, currentDigest)

    drawHorizontalBorders()
    drawVerticalBorders()

    print(time.time())

    pygame.display.flip()

    # if the 'X' button is pressed the window should close:
    Geesh = pygame.event.get()
    if len(Geesh) > 0:
        if Geesh[0].type == QUIT: isDrawingActive = False

    time.sleep(PERIOD_IN_SECONDS)