import logging

# 日志默认的级别为WARNING
# 打印一条消息到终端
logging.warning("Watch out!")

# 不会在终端打印消息
# 此时该日志级别为INFO，低于默认的级别WARNING
logging.info("I told you so.")