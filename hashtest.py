import hashlib
import datetime
import time

print()
print('*** BEGIN ***')
print()

""" CONSTANTS """
secretStringCONSTANT = 'ABCDEFGHIJKLMNOP'
periodIntegerCONSTANT = 1
""" CONSTANTS END """

def setSecret(secretString):
    secretString = secretString
    return secretString

def setPeriod(periodInteger):
    period = periodInteger
    return period

def hashTheInput(stringInput):
    stringToByets = bytes(stringInput, 'utf-8')
    hashedInput = hashlib.sha256()
    hashedInput.update(stringToByets)
    return hashedInput

def getChunkedTime(period):
    currentUnixTime = time.time()
    currentUnixSeconds = int(currentUnixTime)
    chunkedTime = int(currentUnixSeconds / period)
    return chunkedTime

def setInnerString(secret):
    innerString = secret + str(chunkedTime)
    return innerString

""" TO BE FILED UNDER MAIN """

# Set and print the secret
secret = setSecret(secretStringCONSTANT)
print('Secret:               ' + secret)

# Set the period
period = setPeriod(periodIntegerCONSTANT)

# Assign and print chunked time
chunkedTime = getChunkedTime(period)
print('Chunked time:         ' + str(chunkedTime))

# Hash the secret and print the digest (NOT RELEVANT TO FINAL PRODUCT)
hasedSecret = hashTheInput(secret)
hexDigestOfSecret = hasedSecret.hexdigest()
print('SHA256 secret digest: ' + str(hexDigestOfSecret))

# Set inner string
innerString = setInnerString(secret)

# Operations for inner hash
shaInner = hashTheInput(innerString)

# Print inner string and digest (NOT RELEVANT TO FINAL PRODUCT)
print('innerString:          ' + innerString)
hashedInnerAsHex = shaInner.hexdigest()
print('Inner hash:           ' + str(hashedInnerAsHex))

# Operations for outer hash
shaOuter = hashTheInput(secret + hashedInnerAsHex)

# Print the outer digest
outerHexDigest = shaOuter.hexdigest()
print('Outer hash:           ' + outerHexDigest)

print()
print('*** END ***')
print()