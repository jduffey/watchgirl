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

    """
    This algorithm is a variation of the one found here:
    https://garbagecollected.org/2014/09/14/how-google-authenticator-works/
    
    From that page:
    original_secret = xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx
    secret = BASE32_DECODE(TO_UPPERCASE(REMOVE_SPACES(original_secret)))
    input = CURRENT_UNIX_TIME() / 30
    hmac = SHA1(secret + SHA1(secret + input))
    """

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