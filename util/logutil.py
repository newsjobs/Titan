import logging
import logging.config
import os

if not os.path.isdir("./log/"):
        os.makedirs("./log/")

def get_logger():

    logging_path = os.path.split(os.path.realpath(__file__))[0] + os.sep + "logging.conf"
    
    
    logging.config.fileConfig(logging_path)
    logger = logging.getLogger("xmeta")
    return logger