# logging all messages from a program
import logging

# Store logging messages into log.txt file
logging.basicConfig(filename='log.txt', level=logging.ERROR)
try:
     a = int(input('Enter a number: '))
     b = int(input('Enter another number: '))
     c = a / b

except Exception as e:
    logging.exception(e)

else:
    print(f'The result of division: {c}')