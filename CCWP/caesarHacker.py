"""Constants declared here"""
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

""" User operations start here"""
print('This is caesar cipher decoder.')
message_input = input('Enter the message: ')

message = message_input

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]

            else:
                translated = translated + symbol

    #print('Key #%s: %s' % (key, translated))
    print(f'{key}, {translated}')