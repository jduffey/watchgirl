import pygame
from pygame.locals import *
import time
import jedhash
from config import constants as const
from config import number_color_dict

import totp


def get_color(digit_to_use_for_color):
    return number_color_dict[str(int(digit_to_use_for_color, 16) % 4)]


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
    return jedhash.return_the_hash(time_offset)


def update_display():
    pygame.display.flip()


def sleep_between_loops():
    time.sleep(const['PERIOD_IN_SECONDS'] - ((time.time() - loop_start_time) % const['PERIOD_IN_SECONDS']))


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

app_start_time = time.time()
print('\n*** APP START ***')
print(f'Start Time: {app_start_time}')

digest_portion = const['NUM_COLS'] * const['NUM_ROWS']
loop_counter = 0

while is_drawing_active:

    loop_counter += 1

    if loop_counter > 1:
        loop_start_time = time.time()
    else:
        loop_start_time = app_start_time - (app_start_time % const['PERIOD_IN_SECONDS'])
        sleep_between_loops()
        continue

    print(f'\nLoop start: {loop_start_time}')
    print('  ..as int: ' + str(int(loop_start_time)))

    loop_digest = totp.generate_digest(loop_start_time, const['SECRET'], digest_portion)

    digest_char_counter = 0

    outer_list = []
    for which_row in range(0, const['NUM_ROWS']):

        inner_list = []
        for which_column in range(0, const['NUM_COLS']):

            digit_to_use_for_color = loop_digest[digest_char_counter]
            digest_char_counter += 1

            draw_color_icon(which_column, which_row, digit_to_use_for_color)

            inner_list.append(digit_to_use_for_color)

        outer_list.append(inner_list)

    draw_horizontal_borders()
    draw_vertical_borders()
    update_display()

    microseconds_of_loop = 1000 * 1000 * (time.time() - loop_start_time)

    print('  μs taken: ' + str(microseconds_of_loop))
    digest_portion = const['NUM_COLS'] * const['NUM_ROWS']
    print('      TOTP: ' + totp.generate_digest(loop_start_time, const['SECRET'], digest_portion))
    [print(x) for x in outer_list]

    # if the 'X' button is pressed the window should close:
    gotten_events = pygame.event.get()
    print(f'DEBUG Events: {gotten_events}')
    if gotten_events:
        if gotten_events[0].type == QUIT:
            is_drawing_active = False

    sleep_between_loops()