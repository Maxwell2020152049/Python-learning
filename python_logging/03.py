import logging

# 更改显示消息的格式
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

logging.debug("I am debugging.")
logging.info("This is a info.")
logging.warning("This is a warning.")
logging.error("This is an error.")
logging.critical("Find critical!")