import hashlib
import datetime
import time


print()

def setSecret(secretString):
    secretString = secretString
    return secretString

def hashTheInput(stringInput):
    stringToByets = bytes(stringInput, 'utf-8')
    hashedInput = hashlib.sha256()
    hashedInput.update(stringToByets)
    return hashedInput

# Set and print the secret
secret = setSecret('ABCDEFGHIJKLMNOP')
print('Secret:               ' + secret)

hashedInput = hashTheInput(secret)

# hexDigest = hashedInput.hexdigest()
# print('SHA256 secret digest: ' + str(hexDigest))

# digestSize = hashedInput.digest_size
# print('Digest size:          ' + str(digestSize))

# blockSize = hashedInput.block_size
# print('Block size:           ' + str(blockSize))

currentUnixTime = time.time()
currentUnixSeconds = int(currentUnixTime)
print('Unix time:            ' + str(currentUnixTime))
print('Unix seconds:         ' + str(currentUnixSeconds))

period = 2
chunkedTime = int(currentUnixSeconds / period)
print('Chunked time:         ' + str(chunkedTime))

innerString = secret + str(chunkedTime)
innerStringToBytes = bytes(innerString, 'utf-8')
shaInner = hashlib.sha256()
shaInner.update(innerStringToBytes)

print('innerString:          ' + innerString)

hashedInnerAsHex = shaInner.hexdigest()
print('Inner hash:           ' + str(hashedInnerAsHex))

shaOuter = hashlib.sha256()
outerString = str(hashedInnerAsHex)
#print('outerString: ' + outerString)
outerToBytes = bytes(outerString, 'utf-8')
shaOuter.update(outerToBytes)

outerHexDigest = shaOuter.hexdigest()
print('Outer hash:           ' + outerHexDigest)

print()