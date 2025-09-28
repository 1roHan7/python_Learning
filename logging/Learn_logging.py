import logging

""" To this only one time generally right at the beginning of the program"""
logging.basicConfig(level=logging.DEBUG,filename="log.log",filemode="w",
                    format="%(asctime)s -%(levelname)s - %(message)s - %(name)s - %(threadName)s")

logging.debug("This is debug message vallah")
logging.info("This is info message")    
logging.warning("This is warning message")
logging.error("This is error message")  
logging.critical("This is critical message")



