import hashlib
import datetime
import time


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

def returnTheHash(secretInput, periodInput):

    secret = setSecret(secretInput)

    period = setPeriod(periodInput)

    chunkedTime = getChunkedTime(period)

    hasedSecret = hashTheInput(secret)
    
    hexDigestOfSecret = hasedSecret.hexdigest()

    innerString = setInnerString(secret, chunkedTime)

    shaInner = hashTheInput(innerString)

    hashedInnerAsHex = shaInner.hexdigest()

    shaOuter = hashTheInput(secret + hashedInnerAsHex)

    outerHexDigest = shaOuter.hexdigest()

    return outerHexDigest