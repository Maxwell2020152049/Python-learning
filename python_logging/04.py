import logging

# 更改显示消息的格式
# 显示日期/时间
# datefmt可以自定义日期和时间的格式
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',\
    level=logging.DEBUG, datefmt='%Y/%m/%d %H:%M:%S %p')

logging.debug("I am debugging.")
logging.info("This is a info.")
logging.warning("This is a warning.")
logging.error("This is an error.")
logging.critical("Find critical!")