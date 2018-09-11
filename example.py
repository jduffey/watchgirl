import pyotp
import time
import datetime

import pyqrcode

from PIL import Image


# Set the secret
secret = 'ABCDEFGHIJKLMNOP'
totp = pyotp.TOTP(secret)

# Create/open log file
fileName = open('logFile.txt','w+')

# Our loop
for i in range(5):

    currentTotpValue = totp.now()
    currentTime = datetime.datetime.now()

    # Print the TOTP in console
    print(currentTotpValue)
    # Write the TOTP to the log file
    fileName.write('Code is ' + str(currentTotpValue + '\n'))


    # Print the time in console
    print(currentTime)
    # Write the time to the log file
    fileName.write('Time is ' + str(currentTime) + '\n')

    # Create the QR image
    qVar = pyqrcode.create(str(currentTotpValue))
    qVar.png('currentImage.png',scale=30)

    # Tell the user the image was created
    print('QR image generated')

    # Show the image to the user
    with Image.open('currentImage.png') as img:
        img.show()

    # Sleep long enough for the next TOTP to generate
    time.sleep(30)

# Close the log file
fileName.close()





