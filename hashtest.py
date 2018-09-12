import hashlib
import datetime
import time


print()

secret = 'ABCDEFGHIJKLMNOP'
print('Secret:               ' + secret)

stringToByets = bytes(secret, 'utf-8')
m = hashlib.sha256()
m.update(stringToByets)

hexDigest = m.hexdigest()
print('SHA256 hex digest:    ' + str(hexDigest))

digestSize = m.digest_size
print('Digest size:          ' + str(digestSize))

blockSize = m.block_size
print('Block size:           ' + str(blockSize))

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