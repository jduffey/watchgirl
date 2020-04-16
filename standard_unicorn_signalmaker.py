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
import sys
import schedule
from utils import synchronize_time
from utils import get_color


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
        for i in range(digest_portion):
            fill_square(i//2 * height//2, \
                        (i + 2)//2 * height//2, \
                        (i % 2) * width//2, \
                        ((i % 2) + 1) * width//2, \
                        get_color(str(loop_digest[i])))
    if digest_portion == 1:
        fill_all(get_color(str(loop_digest)))


def job(digest_portion):
    start_time = time.time()
    loop_time = int(start_time)
    loop_digest = totp.generate_digest(loop_time, const[sys.argv[1]], digest_portion)

    print(f'  Time is:  {start_time}')
    print(f'Loop time:  {loop_time}')
    print(f'   Digest:  {loop_digest}\n')

    unicorn.clear()
    fill_board(loop_digest, digest_portion)


width, height = unicorn.get_shape()
unicorn.set_layout(unicorn.AUTO)
unicorn.brightness(0.3) # needs to be above ~0.20 to power LEDs
unicorn.rotation(0)

script = sys.argv[0]
secret = sys.argv[1]
digest_portion = int(sys.argv[2])

print(f'\nRunning: {script}')
print(f'Secret:  {secret}: "{const[secret]}"')
print(f'Squares: {digest_portion}\n')

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