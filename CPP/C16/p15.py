# Understanding logging of error messages
import logging

# Store messages into mylog.txt file
# Store only the messages with level equal to or more than that of ERROR
logging.basicConfig(filename='logging.txt', level=logging.ERROR)

# These messages are stored into a file.
logging.error("There is a an error in the program")
logging.critical("There is a problem in the design.")


# These messages are not stored
logging.warning("The project is going slow")
logging.info("You are a junior programmer.")
logging.debug("Line 10 contains syntax error.")