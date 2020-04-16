#!/usr/bin/env python3

try:
    import unicornhat as unicorn
    print('\n*** Unicornhat 8x8 ***\n')
except:
    try:
        import unicornhathd as unicorn
        print('\n*** Unicornhat HD 16x16 ***\n')
    except:
        print('\n*** ERROR: No Unicornhat module detected ***\n')
import time
import totp
import schedule
import sys
from config import constants as const
from config import number_color_dict
from utils import get_color
from utils import synchronize_time


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


def fill_square(bottom_left, bottom_right, top_left, top_right, color):
    for y in range(bottom_left, bottom_right):
        for x in range(top_left, top_right):
            unicorn.set_pixel(x, y, *color)
    unicorn.show()


def fill_all(color):
    unicorn.set_all(*color)
    unicorn.show()


def fill_board(loop_digest, digest_portion):
    if digest_portion == 4:
        # top left
        fill_square(0, height//2, width//2, width, get_color(str(loop_digest[0])))
        # top right
        fill_square(0, height//2, 0, width//2, get_color(str(loop_digest[1])))
        # bottom left
        fill_square(height//2, height, width//2, width, get_color(str(loop_digest[2])))
        # bottom right
        fill_square(height//2, height, 0, width//2, get_color(str(loop_digest[3])))
    if digest_portion == 1:
        fill_all(get_color(str(loop_digest[0])))


def job(digest_portion):
    start_time = time.time()
    loop_time = int(start_time)
    loop_digest = totp.generate_digest(loop_time, const[sys.argv[1]], digest_portion)
    print(f'  Time is:  {start_time}')
    print(f'Loop time:  {loop_time}')
    print(f'   Digest:  {loop_digest}')
    fill_board(loop_digest, digest_portion)
    ms_of_loop = 1000 * (time.time() - start_time)
    print(f'       ms:  {str(ms_of_loop)}\n')


print(f'Secret:  {sys.argv[1]} "{const[sys.argv[1]]}"')
print(f'Squares: {sys.argv[2]}')

digest_portion = int(sys.argv[2])

width, height = unicorn.get_shape()
unicorn.set_layout(unicorn.AUTO)

startup_pixels()

unicorn.brightness(0.5) # needs to be above ~0.20 to power LEDs
unicorn.rotation(0) # ensure rotation has been reset

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