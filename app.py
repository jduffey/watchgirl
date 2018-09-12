import jedhash

secretInput = 'ABCDEFGHIJKLMNOP'
periodInput = 1

def consolePrintBuffer(string):
    print()
    print('*** ' + string + ' ***')
    print()


consolePrintBuffer('BEGIN')

print('Secret:         ' + secretInput)
print('Period (sec):   ' + str(periodInput))

jedhash.returnTheHash(secretInput, periodInput)

outerHash = jedhash.returnTheHash(secretInput, periodInput)
print('Final hash:     ' + outerHash)

consolePrintBuffer('END')