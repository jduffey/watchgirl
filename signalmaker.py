import pygame
from pygame.locals import *
import time
import jedhash
from config import constants as const
from config import number_color_dict


def get_color(digit_to_use_for_color):
    return number_color_dict[digit_to_use_for_color]

def draw_horizontal_borders():
    for i in range(0, const['NUM_ROWS'] + 1):
        top_left_Y = i * (const['BORDER_THICKNESS'] + const['ICON_SIZE_Y'])
        the_rectangle_to_draw = (0, top_left_Y, APP_X_SIZE, const['BORDER_THICKNESS'])
        pygame.draw.rect(screen, const['MY_BLACK'], the_rectangle_to_draw)

def draw_vertical_borders():
    for i in range(0, const['NUM_COLS'] + 1):
        top_left_X = i * (const['BORDER_THICKNESS'] + const['ICON_SIZE_X'])
        the_rectangle_to_draw = (top_left_X, 0, const['BORDER_THICKNESS'], APP_Y_SIZE)
        pygame.draw.rect(screen, const['MY_BLACK'], the_rectangle_to_draw)

def draw_color_icon(which_column, which_row, digit_to_use_for_color):
    top_left_X = const['BORDER_THICKNESS'] + which_column * (const['ICON_SIZE_X'] + const['BORDER_THICKNESS'])
    top_left_Y = const['BORDER_THICKNESS'] + which_row * (const['ICON_SIZE_Y'] + const['BORDER_THICKNESS'])
    bottom_right_X = const['ICON_SIZE_X']
    bottom_right_Y = const['ICON_SIZE_Y']
    the_rectangle_to_draw = (top_left_X, top_left_Y, bottom_right_X, bottom_right_Y)
    pygame.draw.rect(screen, get_color(digit_to_use_for_color), the_rectangle_to_draw)

def generate_digest(time_offset):
    return jedhash.return_the_hash(const['SECRET'], const['PERIOD_IN_SECONDS'], time_offset)

def establish_start_time():
    # force loops to start halfway between periods
    return time.time() - (time.time() % const['PERIOD_IN_SECONDS']) + const['PERIOD_IN_SECONDS'] / 2

def update_display():
    pygame.display.flip()

def print_frame_details():
    print('\nLoop start: ' + str(loop_start_time))
    print('  ms taken: ' + str(milliseconds_of_loop))
    print('   digests: ' + str(digests_generated_this_loop))
    [print(x) for x in outer_list]

def sleep_between_loops():
    time.sleep(const['PERIOD_IN_SECONDS'] - ((time.time() - start_time) % const['PERIOD_IN_SECONDS']))


# Main app functionality below

APP_X_SIZE = const['BORDER_THICKNESS'] +\
             const['NUM_COLS'] * (const['ICON_SIZE_X'] + const['BORDER_THICKNESS'])
APP_Y_SIZE = const['BORDER_THICKNESS'] +\
             const['NUM_ROWS'] * (const['ICON_SIZE_Y'] + const['BORDER_THICKNESS'])

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption(const['WINDOW_TITLE'])
pygame.mouse.set_visible(True)
rectangle_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
screen.blit(rectangle_that_is_the_size_of_the_screen, (0, 0))
update_display()

pygame.init()
is_drawing_active = True

start_time = establish_start_time()
print(start_time)

while is_drawing_active:

    loop_start_time = time.time()

    digests_generated_this_loop = 0

    outer_list = []

    for which_column in range(0, const['NUM_COLS']):

        inner_list = []

        for which_row in range(0, const['NUM_ROWS']):

            digest_time_offset = const['PERIOD_IN_SECONDS'] * (which_column - which_row)

            digest_to_use_for_current_icon = generate_digest(digest_time_offset)
            digests_generated_this_loop += 1

            digit_to_use_for_color = digest_to_use_for_current_icon[0]

            draw_color_icon(which_column, which_row, digit_to_use_for_color)

            inner_list.append(digit_to_use_for_color)

        outer_list.append(inner_list)

    draw_horizontal_borders()
    draw_vertical_borders()
    update_display()

    milliseconds_of_loop = 1000 * (time.time() - loop_start_time)

    print_frame_details()

    # if the 'X' button is pressed the window should close:
    gotten_events = pygame.event.get()
    print(f'DEBUG Events: {gotten_events}')
    if gotten_events:
        if gotten_events[0].type == QUIT:
            is_drawing_active = False

    sleep_between_loops()