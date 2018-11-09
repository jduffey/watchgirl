import pygame
from pygame.locals import *
import time
import jedhash

SECRET = "PRIVATE_KEY_GOES_HERE"
PERIOD_IN_SECONDS = 1

WINDOW_TITLE = 'Identifier #580CD2E889BD - Onett Art Museum Main Entrance'

BORDER_THICKNESS = 10

ICON_SIZE_X = 150
ICON_SIZE_Y = 450

NUMBER_OF_COLUMNS = 6
NUMBER_OF_ROWS = 1

APP_X_SIZE = BORDER_THICKNESS + NUMBER_OF_COLUMNS * ( ICON_SIZE_X + BORDER_THICKNESS )
APP_Y_SIZE = BORDER_THICKNESS + NUMBER_OF_ROWS * ( ICON_SIZE_Y + BORDER_THICKNESS )

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


def getColor(currentDigest, whichIconInCurrentRow, whichRow):
    digitToAssess = currentDigest[whichIconInCurrentRow]

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
        topLeftY = i * ( BORDER_THICKNESS + ICON_SIZE_Y )
        bottomRightX = APP_X_SIZE
        bottomRightY = BORDER_THICKNESS
        theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
        pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

def drawVerticalBorders():
    for i in range(0, NUMBER_OF_COLUMNS + 1):
        topLeftX = i * ( BORDER_THICKNESS + ICON_SIZE_X )
        topLeftY = 0
        bottomRightX = BORDER_THICKNESS
        bottomRightY = APP_Y_SIZE
        theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
        pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

def drawColorIcon(whichIconInCurrentRow, whichRow, currentDigest):
    topLeftX = BORDER_THICKNESS + whichIconInCurrentRow * ( ICON_SIZE_X + BORDER_THICKNESS )
    topLeftY = BORDER_THICKNESS + whichRow * ( ICON_SIZE_Y + BORDER_THICKNESS )
    bottomRightX = ICON_SIZE_X
    bottomRightY = ICON_SIZE_Y
    theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
    pygame.draw.rect(screen, getColor(currentDigest, whichIconInCurrentRow, whichRow), theRectangleToDraw)

def generateDigestForCurrentTime(whichIconInCurrentRow):
    return jedhash.returnTheHash(SECRET, PERIOD_IN_SECONDS, whichIconInCurrentRow)

def validateNumberOfColumns():
        if(NUMBER_OF_COLUMNS > SIZE_OF_DIGEST_USED):
            print('ERROR: Too many columns! Max size is ' + str(SIZE_OF_DIGEST_USED))
        return NUMBER_OF_COLUMNS <= SIZE_OF_DIGEST_USED

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption(WINDOW_TITLE)
pygame.mouse.set_visible(True)
rectangleThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
rectangleThatIsTheSizeOfTheScreen.fill(MY_WHITE)
screen.blit(rectangleThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

pygame.init()
isDrawingActive = True

if not validateNumberOfColumns():
    exit()

while isDrawingActive:

    for whichRow in range(0, NUMBER_OF_ROWS):
        offset = whichRow * PERIOD_IN_SECONDS
        currentDigest = generateDigestForCurrentTime(offset)
        for whichIconInCurrentRow in range(0, NUMBER_OF_COLUMNS):
            drawColorIcon(whichIconInCurrentRow, whichRow, currentDigest)

    drawHorizontalBorders()
    drawVerticalBorders()

    print(time.time())

    pygame.display.flip()

    # if the 'X' button is pressed the window should close:
    Geesh = pygame.event.get()
    if len(Geesh) > 0:
        if Geesh[0].type == QUIT: isDrawingActive = False

    time.sleep(PERIOD_IN_SECONDS)