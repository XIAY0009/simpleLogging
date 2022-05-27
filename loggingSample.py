#Python3 logging 

import logging 
from datetime import datetime 

#Sets the color of the message 
def Message(severity, message): 
    
    COLORS = { 
        0: '\033[1;92m', 
        1: '\033[1;36m', 
        2: '\033[1;95m', 
        3: '\033[1;33m', 
        4: '\033[1;91m'
    }
    return COLORS[severity] + " " + message + "\033[0m"

#A different log file should be generated for each time it restarts 
dtString = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

#Logs into a file instead of the console
# Remove all handlers associated with the root logger object.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

tsFileName = dtString + ".log"
#Logs any message from the DEBUG level  
logging.basicConfig(level=logging.DEBUG, filename=tsFileName, filemode='w', format='%(asctime)s %(levelname)9s: %(message)s', datefmt='%Y-%M-%d %H:%M:%S')

logging.debug(Message(0, "A debug message"))
logging.info(Message(1, "An info message"))
logging.warning(Message(2, "A warning message"))
logging.critical(Message(3, "A critical message"))
logging.error(Message(4, "An error message"))
