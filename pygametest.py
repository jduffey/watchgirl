import pygame
from pygame.locals import *
import time
import jedhash

SECRET = "PRIVATE_KEY_GOES_HERE"
PERIOD_IN_SECONDS = 1

WINDOW_TITLE = 'Identifier #580CD2E889BD - Onett Art Museum Main Entrance'

BORDER_THICKNESS = 10
SQUARE_WIDTH = 150

NUMBER_OF_COLUMNS = 6
NUMBER_OF_ROWS = 4

APP_X_SIZE = BORDER_THICKNESS + NUMBER_OF_COLUMNS * ( SQUARE_WIDTH + BORDER_THICKNESS )
APP_Y_SIZE = BORDER_THICKNESS + NUMBER_OF_ROWS * ( SQUARE_WIDTH + BORDER_THICKNESS )

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

SIZE_OF_DIGEST_USED = 64


def getColor(currentDigest, whichSquareInCurrentRow, whichRow):
    digitToAssess = currentDigest[whichSquareInCurrentRow]

    case1 = digitToAssess == '0' or digitToAssess == '8'
    case2 = digitToAssess == '1' or digitToAssess == '9'
    case3 = digitToAssess == '2' or digitToAssess == 'a'
    case4 = digitToAssess == '3' or digitToAssess == 'b'
    case5 = digitToAssess == '4' or digitToAssess == 'c'
    case6 = digitToAssess == '5' or digitToAssess == 'd'
    case7 = digitToAssess == '6' or digitToAssess == 'e'
    case8 = digitToAssess == '7' or digitToAssess == 'f'

    if case1:
        nextColor = MY_RED
    if case2:
        nextColor = MY_ORANGE
    if case3:
        nextColor = MY_YELLOW
    if case4:
        nextColor = MY_GREEN
    if case5:
        nextColor = MY_BLUE
    if case6:
        nextColor = MY_VIOLET
    if case7:
        nextColor = MY_BROWN
    if case8:
        nextColor = MY_GREY
    return nextColor

def drawHorizontalBorders():
    for i in range(0, NUMBER_OF_ROWS + 1):
        topLeftX = 0
        topLeftY = i * ( BORDER_THICKNESS + SQUARE_WIDTH )
        bottomRightX = APP_X_SIZE
        bottomRightY = BORDER_THICKNESS
        theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
        pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

def drawVerticalBorders():
    for i in range(0, NUMBER_OF_COLUMNS + 1):
        topLeftX = i * ( BORDER_THICKNESS + SQUARE_WIDTH )
        topLeftY = 0
        bottomRightX = BORDER_THICKNESS
        bottomRightY = APP_Y_SIZE
        theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
        pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

def drawColorSquare(whichSquareInCurrentRow, whichRow, currentDigest):
    topLeftX = BORDER_THICKNESS + whichSquareInCurrentRow * ( SQUARE_WIDTH + BORDER_THICKNESS )
    topLeftY = BORDER_THICKNESS + whichRow * ( SQUARE_WIDTH + BORDER_THICKNESS )
    bottomRightX = SQUARE_WIDTH
    bottomRightY = SQUARE_WIDTH
    theSquareToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
    pygame.draw.rect(screen, getColor(currentDigest, whichSquareInCurrentRow, whichRow), theSquareToDraw)

def generateDigestForCurrentTime(whichSquareInCurrentRow):
    return jedhash.returnTheHash(SECRET, PERIOD_IN_SECONDS, whichSquareInCurrentRow)

def validateNumberOfColumns():
        if(NUMBER_OF_COLUMNS > SIZE_OF_DIGEST_USED):
            print('ERROR: Too many columns! Max size is ' + str(SIZE_OF_DIGEST_USED))
        return NUMBER_OF_COLUMNS <= SIZE_OF_DIGEST_USED

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption(WINDOW_TITLE)
pygame.mouse.set_visible(True)
squareThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
squareThatIsTheSizeOfTheScreen.fill(MY_WHITE)
screen.blit(squareThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

pygame.init()
isDrawingActive = True

if not validateNumberOfColumns():
    exit()

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