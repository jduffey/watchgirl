import jedhash

import pyqrcode

from PIL import Image

import time

secretInput = 'ABCDEFGHIJKLMNOP'
periodInput = 1

def consolePrintBuffer(string):
    print()
    print('*** ' + string + ' ***')
    print()


consolePrintBuffer('BEGIN')

print('Secret:         ' + secretInput)
print('Period (sec):   ' + str(periodInput))

for i in range(10):

    outerHash = jedhash.returnTheHash(secretInput, periodInput)
    print('Final hash:     ' + outerHash)

    qrCurrent = pyqrcode.create(str(outerHash))
    qrCurrent.png('qrCurrent.png', scale = 20)
    print('(Debug: image written)')

    with Image.open('qrCurrent.png') as img:
        print('BEFORE Command to open image')
        img.show()
        print('AFTER Command to open image')

    time.sleep(1)

consolePrintBuffer('END')