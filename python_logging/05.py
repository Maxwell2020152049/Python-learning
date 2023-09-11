import logging

# 创建一个记录器，并设置日志等级
logger = logging.Logger("simple_example")
logger.setLevel(logging.DEBUG)

# 创建一个控制台处理器，并设置日志等级
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建一个格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 把格式器添加到处理器上
ch.setFormatter(formatter)

# 把处理器添加到记录器上
logger.addHandler(ch)

# 应用代码
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')