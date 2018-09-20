import jwtgen
import datetime
import time

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

print('  Delay (seconds): ' + str(delayBetweenCodesInSeconds))
print('Codes to generate: ' + str(codesToGenerate))
print()

for i in range(codesToGenerate):

    currentTime = datetime.datetime.now()
    expirationJWT = currentTime+datetime.timedelta(minutes=10)

    iat = currentTime
    exp = expirationJWT

    generated_jwt = jwtgen.genjwt(iss, iat, exp, secret, alg)
    jwtasstring = str(generated_jwt.decode('utf-8'))

    jwtsplit = jwtasstring.split('.')
    print('   JWT header:  ' + jwtsplit[0])
    print('  JWT payload:  ' + jwtsplit[1])
    print('JWT signature:  ' + jwtsplit[2])
    print('          iat:  ' + str(iat))
    print('     unix-iat:  ' + str(time.mktime(iat.timetuple())))
    print('          exp:  ' + str(exp))
    print('     unix-exp:  ' + str(time.mktime(exp.timetuple())))

    jwtimage = pyqrcode.create(str(jwtasstring))
    jwtimage.png('jwtimage.png', scale = 5)
    print('(Debug: image written)')

    with Image.open('jwtimage.png') as img:
        print('(Debug: BEFORE command to open image)')
        img.show()
        print('(Debug: AFTER command to open image)')

    print()

    notOnTheLastIteration = i < codesToGenerate - 1

    if notOnTheLastIteration:
        time.sleep(delayBetweenCodesInSeconds)

consolePrintBuffer('END')