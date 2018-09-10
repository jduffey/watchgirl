import pyotp

totp = pyotp.TOTP('ABCDEFGHIJKLMNOP')

print(totp.now())
