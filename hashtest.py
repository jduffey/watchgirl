import hashlib
import datetime
import time


secretStringCONSTANT = 'ABCDEFGHIJKLMNOP'
periodIntegerCONSTANT = 1


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

def setInnerString(secret, chunkedTime):
    innerString = secret + str(chunkedTime)
    return innerString

def main():

    secret = setSecret(secretStringCONSTANT)
    print('Secret:               ' + secret)

    period = setPeriod(periodIntegerCONSTANT)

    chunkedTime = getChunkedTime(period)
    print('Chunked time:         ' + str(chunkedTime))

    hasedSecret = hashTheInput(secret)
    hexDigestOfSecret = hasedSecret.hexdigest()
    print('SHA256 secret digest: ' + str(hexDigestOfSecret))

    innerString = setInnerString(secret, chunkedTime)

    shaInner = hashTheInput(innerString)

    print('innerString:          ' + innerString)
    hashedInnerAsHex = shaInner.hexdigest()
    print('Inner hash:           ' + str(hashedInnerAsHex))

    shaOuter = hashTheInput(secret + hashedInnerAsHex)

    outerHexDigest = shaOuter.hexdigest()
    print('Outer hash:           ' + outerHexDigest)