"""Constants declared here"""
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

""" User operations start here"""
mode_input = input('Enter the mode of operation: ')
message_input = input('Enter the message: ')
key_input = eval(input('Enter the key: '))

message = message_input
key = key_input
mode = mode_input

translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt' or 'e':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt' or 'd':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        translatedIndex = translatedIndex + symbol

print(translated)

