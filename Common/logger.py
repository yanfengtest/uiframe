import logging

from PO.Common.dir_config import log_dir


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name="root",
                 level="INFO",
                 file=None,
                 format = "%(filename)s-%(lineno)s-%(name)s-%(levelname)s-%(message)s-%(asctime)s"):
        #logger = logging.getLogger(name)
        super().__init__(name)

        #设置级别
        self.setLevel(level)
        fmt = logging.Formatter(format)
        #初始化处理器handler
        if  file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        steam_handler = logging.StreamHandler()

        #设置handler级别
        steam_handler.setLevel(level)
        steam_handler.setFormatter(fmt)
        self.addHandler(steam_handler)
file = log_dir+"\python25.txt"
logger = LoggerHandler(name="yanfeng",file=file)







