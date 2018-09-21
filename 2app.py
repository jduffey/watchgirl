import jwtgen
import datetime
import time
import config

import pyqrcode

from PIL import Image

import time

delayBetweenCodesInSeconds = config.settings['delayBetweenCodesInSeconds']
codesToGenerate = config.settings['codesToGenerate']
qrCodeSize = config.settings['qrCodeSize']

secret = config.signature['secret']
alg = config.header['alg']


def consolePrintBuffer(string):
    print()
    print('*** ' + string + ' ***')
    print()

def consolePrintJWTstats():
    jwtsplit = jwtasstring.split('.')
    print('JWT head:  ' + jwtsplit[0])
    print('JWT payl:  ' + jwtsplit[1])
    print('JWT sign:  ' + jwtsplit[2])
    print('     iat:  ' + str(iat))
    print('unix-iat:  ' + str(time.mktime(iat.timetuple())))
    print('     exp:  ' + str(exp))
    print('unix-exp:  ' + str(time.mktime(exp.timetuple())))
    print('     iss:  ' + config.payload['iss'])
    print('    desc:  ' + config.payload['desc'])


consolePrintBuffer('BEGIN')

print('  Delay (seconds): ' + str(delayBetweenCodesInSeconds))
print('Codes to generate: ' + str(codesToGenerate))
print('     QR code size: ' + str(qrCodeSize))
print()

for i in range(codesToGenerate):

    currentTime = datetime.datetime.now()
    expirationJWT = currentTime+datetime.timedelta(minutes=10)

    iat = currentTime
    exp = expirationJWT

    generated_jwt = jwtgen.genjwt(config.payload['iss'], config.payload['desc'], iat, exp, secret, alg)
    jwtasstring = str(generated_jwt.decode('utf-8'))

    consolePrintJWTstats()

    # jwtsplit = jwtasstring.split('.')
    # print('JWT head:  ' + jwtsplit[0])
    # print('JWT payl:  ' + jwtsplit[1])
    # print('JWT sign:  ' + jwtsplit[2])
    # print('     iat:  ' + str(iat))
    # print('unix-iat:  ' + str(time.mktime(iat.timetuple())))
    # print('     exp:  ' + str(exp))
    # print('unix-exp:  ' + str(time.mktime(exp.timetuple())))
    # print('     iss:  ' + config.payload['iss'])
    # print('    desc:  ' + config.payload['desc'])

    jwtimage = pyqrcode.create(str(jwtasstring))
    jwtimage.png('jwtimage.png', scale = qrCodeSize)
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