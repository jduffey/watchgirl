import pygame
from pygame.locals import *
import time
import jedhash
from config import constants


SECRET = constants['SECRET']
PERIOD_IN_SECONDS = constants['PERIOD_IN_SECONDS']
WINDOW_TITLE = constants['WINDOW_TITLE']
BORDER_THICKNESS = constants['BORDER_THICKNESS']
ICON_SIZE_X = constants['ICON_SIZE_X']
ICON_SIZE_Y = constants['ICON_SIZE_Y']
NUMBER_OF_COLUMNS = constants['NUMBER_OF_COLUMNS']
NUMBER_OF_ROWS = constants['NUMBER_OF_ROWS']
MY_RED = constants['MY_RED']
MY_ORANGE = constants['MY_ORANGE']
MY_YELLOW = constants['MY_YELLOW']
MY_GREEN = constants['MY_GREEN']
MY_BLUE = constants['MY_BLUE']
MY_VIOLET = constants['MY_VIOLET']
MY_BROWN = constants['MY_BROWN']
MY_GREY = constants['MY_GREY']
MY_BLACK = constants['MY_BLACK']
MY_WHITE = constants['MY_WHITE']

number_color_dict = {
    '0': MY_RED,
    '1': MY_RED,
    '2': MY_ORANGE,
    '3': MY_ORANGE,
    '4': MY_YELLOW,
    '5': MY_YELLOW,
    '6': MY_GREEN,
    '7': MY_GREEN,
    '8': MY_BLUE,
    '9': MY_BLUE,
    'a': MY_VIOLET,
    'b': MY_VIOLET,
    'c': MY_BROWN,
    'd': MY_BROWN,
    'e': MY_GREY,
    'f': MY_GREY
}


def get_color(digit_to_use_for_color):
    return number_color_dict[digit_to_use_for_color]

def draw_horizontal_borders():
    for i in range(0, NUMBER_OF_ROWS + 1):
        top_left_X = 0
        top_left_Y = i * ( BORDER_THICKNESS + ICON_SIZE_Y )
        bottom_right_X = APP_X_SIZE
        bottom_right_Y = BORDER_THICKNESS
        the_rectangle_to_draw = (top_left_X, top_left_Y, bottom_right_X, bottom_right_Y)
        pygame.draw.rect(screen, MY_BLACK, the_rectangle_to_draw)

def draw_vertical_borders():
    for i in range(0, NUMBER_OF_COLUMNS + 1):
        top_left_X = i * ( BORDER_THICKNESS + ICON_SIZE_X )
        top_left_Y = 0
        bottom_right_X = BORDER_THICKNESS
        bottom_right_Y = APP_Y_SIZE
        the_rectangle_to_draw = (top_left_X, top_left_Y, bottom_right_X, bottom_right_Y)
        pygame.draw.rect(screen, MY_BLACK, the_rectangle_to_draw)

def draw_color_icon(which_column, which_row, digit_to_use_for_color):
    top_left_X = BORDER_THICKNESS + which_column * ( ICON_SIZE_X + BORDER_THICKNESS )
    top_left_Y = BORDER_THICKNESS + which_row * ( ICON_SIZE_Y + BORDER_THICKNESS )
    bottom_right_X = ICON_SIZE_X
    bottom_right_Y = ICON_SIZE_Y
    the_rectangle_to_draw = (top_left_X, top_left_Y, bottom_right_X, bottom_right_Y)
    pygame.draw.rect(screen, get_color(digit_to_use_for_color), the_rectangle_to_draw)

def generate_digest(time_offset):
    return jedhash.return_the_hash(SECRET, PERIOD_IN_SECONDS, time_offset)

def establish_start_time():
    # force loops to start halfway between periods
    return time.time() - (time.time() % PERIOD_IN_SECONDS) + PERIOD_IN_SECONDS / 2


APP_X_SIZE = BORDER_THICKNESS + NUMBER_OF_COLUMNS * ( ICON_SIZE_X + BORDER_THICKNESS )
APP_Y_SIZE = BORDER_THICKNESS + NUMBER_OF_ROWS * ( ICON_SIZE_Y + BORDER_THICKNESS )

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption(WINDOW_TITLE)
pygame.mouse.set_visible(True)
rectangle_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
rectangle_that_is_the_size_of_the_screen.fill(MY_WHITE)
screen.blit(rectangle_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()

pygame.init()
is_drawing_active = True


start_time = establish_start_time()
print(start_time)

while is_drawing_active:

    print()

    loop_start_time = time.time()
    print('Loop start: ' + str(loop_start_time))

    digests_generated_this_loop = 0

    outer_list = []

    for which_column in range(0, NUMBER_OF_COLUMNS):

        inner_list = []

        for which_row in range(0, NUMBER_OF_ROWS):

            digest_time_offset = PERIOD_IN_SECONDS * (which_column - which_row)

            digest_to_use_for_current_icon = generate_digest(digest_time_offset)
            digests_generated_this_loop += 1

            digit_to_use_for_color = digest_to_use_for_current_icon[0]

            draw_color_icon(which_column, which_row, digit_to_use_for_color)

            inner_list.append(digit_to_use_for_color)

        outer_list.append(inner_list)

    draw_horizontal_borders()
    draw_vertical_borders()

    pygame.display.flip()

    milliseconds_of_loop = 1000 * (time.time() - loop_start_time)

    print('  ms taken: ' + str(milliseconds_of_loop))
    print('   digests: ' + str(digests_generated_this_loop))
    for list in outer_list:
        print(list)

    # if the 'X' button is pressed the window should close:
    gotten_events = pygame.event.get()
    if len(gotten_events) > 0:
        if gotten_events[0].type == QUIT: is_drawing_active = False

    time.sleep(PERIOD_IN_SECONDS - ((time.time() - start_time) % PERIOD_IN_SECONDS))