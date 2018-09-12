import jedhash

secretInput = 'ABCDEFGHIJKLMNOP'
periodInput = 1

def consolePrintBuffer(string):
    print()
    print('*** ' + string + ' ***')
    print()


consolePrintBuffer('BEGIN')

jedhash.main(secretInput, periodInput)

consolePrintBuffer('END')