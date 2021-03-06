import pygame
from pygame.locals import *
import time
import totp
from config import constants as const
from config import number_color_dict
import schedule


def get_color(digit_to_use_for_color):
    return number_color_dict[int(digit_to_use_for_color, 16) % 4]


def draw_horizontal_borders():
    for i in range(0, const['NUM_ROWS'] + 1):
        top_left_Y = i * (const['BORDER_THICKNESS'] + const['ICON_SIZE_Y'])
        the_rectangle_to_draw = (0, top_left_Y, APP_X_SIZE, const['BORDER_THICKNESS'])
        pygame.draw.rect(screen, const['BLACK'], the_rectangle_to_draw)


def draw_vertical_borders():
    for i in range(0, const['NUM_COLS'] + 1):
        top_left_X = i * (const['BORDER_THICKNESS'] + const['ICON_SIZE_X'])
        the_rectangle_to_draw = (top_left_X, 0, const['BORDER_THICKNESS'], APP_Y_SIZE)
        pygame.draw.rect(screen, const['BLACK'], the_rectangle_to_draw)


def draw_color_icon(which_column, which_row, digit_to_use_for_color):
    top_left_X = const['BORDER_THICKNESS'] + which_column * (const['ICON_SIZE_X'] + const['BORDER_THICKNESS'])
    top_left_Y = const['BORDER_THICKNESS'] + which_row * (const['ICON_SIZE_Y'] + const['BORDER_THICKNESS'])
    bottom_right_X = const['ICON_SIZE_X']
    bottom_right_Y = const['ICON_SIZE_Y']
    the_rectangle_to_draw = (top_left_X, top_left_Y, bottom_right_X, bottom_right_Y)
    pygame.draw.rect(screen, get_color(digit_to_use_for_color), the_rectangle_to_draw)


def update_display():
    pygame.display.flip()


def job(digest_portion):
    start_time = time.time()
    loop_time = int(start_time)
    print(f'  Time is:  {start_time}')
    print(f'Loop time:  {loop_time}\n')

    loop_digest_01 = totp.generate_digest(loop_time, const['SECRET_01'], digest_portion)
    loop_digest_02 = totp.generate_digest(loop_time, const['SECRET_02'], digest_portion)
    loop_digest_03 = totp.generate_digest(loop_time, const['SECRET_03'], digest_portion)
    loop_digests = [loop_digest_01, loop_digest_02, loop_digest_03]

    signal_placement = 0
    for loop_digest in loop_digests:

        digest_char_counter = 0
        for which_row in range(0, const['NUM_ROWS']):
            for which_column in range(0, const['NUM_COLS']):
                digit_to_use_for_color = loop_digest[digest_char_counter]
                digest_char_counter += 1
                draw_color_icon(which_column + signal_placement, which_row, digit_to_use_for_color)
        signal_placement += 2


    draw_horizontal_borders()
    draw_vertical_borders()
    update_display()

    microseconds_of_loop = 1000 * 1000 * (time.time() - start_time)

    print('   micro s: ' + str(microseconds_of_loop))
    digest_portion = const['NUM_COLS'] * const['NUM_ROWS']
    print('      TOTP: ' + totp.generate_digest(loop_time, const['SECRET_03'], digest_portion))


digest_portion = const['NUM_COLS'] * const['NUM_ROWS']

APP_X_SIZE = const['BORDER_THICKNESS'] +\
             const['NUM_COLS'] * 3 * (const['ICON_SIZE_X'] + const['BORDER_THICKNESS'])
APP_Y_SIZE = const['BORDER_THICKNESS'] +\
             const['NUM_ROWS'] * (const['ICON_SIZE_Y'] + const['BORDER_THICKNESS'])

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption(const['WINDOW_TITLE'])
pygame.mouse.set_visible(True)
rectangle_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
screen.blit(rectangle_that_is_the_size_of_the_screen, (0, 0))
update_display()

pygame.init()

schedule.every().minute.at(":00").do(job, digest_portion)
schedule.every().minute.at(":05").do(job, digest_portion)
schedule.every().minute.at(":10").do(job, digest_portion)
schedule.every().minute.at(":15").do(job, digest_portion)
schedule.every().minute.at(":20").do(job, digest_portion)
schedule.every().minute.at(":25").do(job, digest_portion)
schedule.every().minute.at(":30").do(job, digest_portion)
schedule.every().minute.at(":35").do(job, digest_portion)
schedule.every().minute.at(":40").do(job, digest_portion)
schedule.every().minute.at(":45").do(job, digest_portion)
schedule.every().minute.at(":50").do(job, digest_portion)
schedule.every().minute.at(":55").do(job, digest_portion)

print('\n*** APP START ***')
print(f'Start Time: {time.time()}')

while True:
    schedule.run_pending()
