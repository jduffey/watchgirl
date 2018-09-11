import pyotp
import time
import datetime

import pyqrcode

from PIL import Image


secret = 'ABCDEFGHIJKLMNOP'
totp = pyotp.TOTP(secret)

fileName = open('logFile.txt','w+')

for i in range(5):

    currentTotpValue = totp.now()
    currentTime = datetime.datetime.now()

    print(currentTotpValue)
    fileName.write('Code is ' + str(currentTotpValue + '\n'))

    print(currentTime)
    fileName.write('Time is ' + str(currentTime) + '\n')

    qVar = pyqrcode.create(str(currentTotpValue))
    qVar.png('currentImage.png',scale=6)

    print('QR image generated')

    with Image.open('currentImage.png') as img:
        img.show()

    time.sleep(30)

fileName.close()





