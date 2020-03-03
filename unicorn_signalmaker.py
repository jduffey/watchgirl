#!/usr/bin/env python3

import sys
import unicornhathd as unicorn
import time
import totp
from config import constants as const
from config import number_color_dict
import os


def startup_pixels():
    for pairing in [(0, const['WHITE']), (90, const['YELLOW']),
                    (180, const['CYAN']), (270, const['MAGENTA'])]:
        unicorn.rotation(pairing[0])
        for i in range(width):
            unicorn.set_pixel(i, i, *pairing[1])
            for y in range(height):
                unicorn.set_pixel(i, y, *pairing[1])
            for x in range(width):
                unicorn.set_pixel(x, i, *pairing[1])
            unicorn.show()
            time.sleep(0.01)


def synchronize_time():
    command = 'sudo ntpdate -s'
    target = 'time.nist.gov'
    print(f'Syncing time with {target}')
    os.system(command + ' ' + target)


def fill_square(bottom_left, bottom_right, top_left, top_right, r, g, b):
    for y in range(bottom_left, bottom_right):
        for x in range(top_left, top_right):
            unicorn.set_pixel(x,y,r,g,b)
    unicorn.show()


def fill_4_squares():
        # top left
        fill_square(0, height//2, width//2, width, *get_color(str(loop_digest[0])))
        # top right
        fill_square(0, height//2, 0, width//2, *get_color(str(loop_digest[1])))
        # bottom left
        fill_square(height//2, height, width//2, width, *get_color(str(loop_digest[2])))
        # bottom right
        fill_square(height//2, height, 0, width//2, *get_color(str(loop_digest[3])))


def get_color(digit_to_use_for_color):
    return number_color_dict[str(int(digit_to_use_for_color, 16) % 4)]


def sleep_between_loops():
    time.sleep(const['PERIOD_IN_SECONDS'] - ((time.time() - loop_start_time) % const['PERIOD_IN_SECONDS']))


print(f'Secret: {sys.argv[1]} "{const[sys.argv[1]]}"')

width, height = unicorn.get_shape()
unicorn.set_layout(unicorn.AUTO)

startup_pixels()

unicorn.brightness(0.5) # needs to be above ~0.20 to power LEDs
unicorn.rotation(0)

synchronize_time()

is_unicorn_active = True

digest_portion = 4
loop_counter = 0

app_start_time = time.time()
print('\n*** APP START ***')
print(f'Start Time: {app_start_time}')

while is_unicorn_active:

    if loop_counter > 1:
        loop_counter += 1
        actual_start_time = time.time()
        loop_start_time = int(actual_start_time)
    else:
        loop_counter += 1
        loop_start_time = app_start_time - (app_start_time % const['PERIOD_IN_SECONDS'])
        sleep_between_loops()
        continue

    loop_digest = totp.generate_digest(loop_start_time, const[sys.argv[1]], digest_portion)

    print(f'\n Loop count: {loop_counter}')
    print(f'Actual time: {actual_start_time}')
    print(f'   Time msg: {loop_start_time}')
    print(f'     Digest: {loop_digest}')

    fill_4_squares()

    end_time = time.time()
    ms_of_loop = 1000 * (actual_start_time - loop_start_time)
    print(f'         ms: {str(ms_of_loop)}')
    print(f'   End time: {end_time}')

    sleep_between_loops()