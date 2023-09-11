import logging

# 使用 Python 3.8.10
# 不支持 basicConfig方法的encoding参数
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# 日志文件的级别为最低的DEBUG
# 所有级别的日志都会被记录到目标文件中
logging.debug("I am debugging.")
logging.info("This is a info.")
logging.warning("This is a warning.")
logging.error("This is an error.")
logging.critical("Find critical!")

