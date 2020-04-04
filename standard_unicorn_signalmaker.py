#!/usr/bin/env python3

try:
    import unicornhat as unicorn
except ExplicitException:
    try:
        import unicornhathd as unicorn
    except:
        pass
import time
import totp
from config import constants as const
from config import number_color_dict
import os
import sys
import schedule


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
            time.sleep(0.04)


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


def fill_4_squares(loop_digest):
        # bottom right
        fill_square(0, height//2, width//2, width, *get_color(str(loop_digest[3])))
        # top right
        fill_square(0, height//2, 0, width//2, *get_color(str(loop_digest[1])))
        # bottom left
        fill_square(height//2, height, width//2, width, *get_color(str(loop_digest[2])))
        # top left
        fill_square(height//2, height, 0, width//2, *get_color(str(loop_digest[0])))


def get_color(digit_to_use_for_color):
    return number_color_dict[int(digit_to_use_for_color, 16) % 4]


def job(digest_portion):
    start_time = time.time()
    loop_time = int(start_time)
    loop_digest = totp.generate_digest(loop_time, const[sys.argv[1]], digest_portion)

    print(f'  Time is:  {start_time}')
    print(f'Loop time:  {loop_time}')
    print(f'   Digest:  {loop_digest}\n')

    fill_4_squares(loop_digest)


width, height = unicorn.get_shape()
unicorn.set_layout(unicorn.AUTO)
unicorn.brightness(0.5) # needs to be above ~0.20 to power LEDs
unicorn.rotation(0)

digest_portion = 4

print(f'Secret: {sys.argv[1]} "{const[sys.argv[1]]}"')

startup_pixels()

synchronize_time()

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
print(f'   Time is: {time.time()}\n')

while True:
    schedule.run_pending()