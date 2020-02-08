import unicornhat as unicorn
import time
import totp
from config import constants as const
from config import number_color_dict
from random import randint


def fill_square(bottom_left, bottom_right, top_left, top_right, r, g, b):
    for y in range(bottom_left, bottom_right):
        for x in range(top_left, top_right):
            unicorn.set_pixel(x,y,r,g,b)
            unicorn.show()


def get_color(digit_to_use_for_color):
    return number_color_dict[str(int(digit_to_use_for_color, 16) % 4)]


def sleep_between_loops():
    time.sleep(const['PERIOD_IN_SECONDS'] - ((time.time() - loop_start_time) % const['PERIOD_IN_SECONDS']))


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.25) # needs to be above ~0.20
width,height=unicorn.get_shape()

for i in range(200):
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(127, 255)
    g = randint(127, 255)
    b = randint(127, 255)
    unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()

# Main app functionality below

is_unicorn_active = True

digest_portion = 64
loop_counter = 0

app_start_time = time.time()
print('\n*** APP START ***')
print(f'Start Time: {app_start_time}')

while is_unicorn_active:

    loop_counter += 1

    if loop_counter > 1:
        loop_start_time = int(time.time())
    else:
        loop_start_time = app_start_time - (app_start_time % const['PERIOD_IN_SECONDS'])
        sleep_between_loops()
        continue

    print(f'\nLoop start: {loop_start_time}')

    loop_digest = totp.generate_digest(loop_start_time, const['SECRET'], digest_portion)

    digest_char_counter = 0

    outer_list = []
    for which_row in range(0, const['NUM_ROWS']):

        inner_list = []
        for which_column in range(0, const['NUM_COLS']):

            digit_to_use_for_color = loop_digest[digest_char_counter]
            digest_char_counter += 1

            #draw_color_icon(which_column, which_row, digit_to_use_for_color)

            inner_list.append(digit_to_use_for_color)

        outer_list.append(inner_list)

    print(f'TOTP: {loop_digest}')
    [print(x) for x in outer_list]

    #fill_square(height//2, height, width//2, width, *get_color(str(loop_digest[0])))
    #fill_square(height//2, height, 0, width//2, *get_color(str(loop_digest[1])))
    #fill_square(0, height//2, width//2, width, *get_color(str(loop_digest[2])))
    #fill_square(0, height//2, 0, width//2, *get_color(str(loop_digest[3])))

    shift = height//4
    square_size = 2

    # use 16 squares
    for i in range(16):
        fill_square(height - (i // 4 + 1) * shift, height - (i // 4) * shift, \
                    width - (i % 4 + 1) * shift, width - (i % 4) * shift, \
                    *get_color(str(loop_digest[i])))

    # use all of digest
    #for i in range(len(loop_digest)):
    #    unicorn.set_pixel(i % 8, i // 8, *get_color(str(loop_digest[i])))
    #    unicorn.show()
    #    time.sleep(pause_between_pixel)

    ms_of_loop = 1000 * (time.time() - loop_start_time)
    print(f'ms: {str(ms_of_loop)}')


    sleep_between_loops()