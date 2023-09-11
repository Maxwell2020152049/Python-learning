# myapp.py
import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')

    # 运行导入模块的函数时，输出日志
    # 其级别限制来自于本地环境
    mylib.do_something()

    logging.info('Finished')

if __name__ == '__main__':
    main()