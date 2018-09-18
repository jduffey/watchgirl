import jwtgen
import datetime

import pyqrcode

from PIL import Image

import time

delayBetweenCodesInSeconds = 2
codesToGenerate = 5

iss = 'Meetup Group, Event #006'
secret = 'ABC'
alg = 'HS256'


def consolePrintBuffer(string):
    print()
    print('*** ' + string + ' ***')
    print()


consolePrintBuffer('BEGIN')

for i in range(codesToGenerate):

    currentTime = datetime.datetime.now()
    expirationJWT = currentTime+datetime.timedelta(minutes=10)

    iat = currentTime
    exp = expirationJWT

    generated_jwt = jwtgen.genjwt(iss, iat, exp, secret, alg)
    jwtasstring = str(generated_jwt.decode('utf-8'))

    print(jwtasstring)
    print('iat:   ' + str(iat))
    print('exp:   ' + str(exp))

    jwtimage = pyqrcode.create(str(jwtasstring))
    jwtimage.png('jwtimage.png', scale = 5)
    print('(Debug: image written)')

    with Image.open('jwtimage.png') as img:
        print('(Debug: BEFORE command to open image)')
        img.show()
        print('(Debug: AFTER command to open image)')

    if i < codesToGenerate - 1:
        time.sleep(delayBetweenCodesInSeconds)

consolePrintBuffer('END')