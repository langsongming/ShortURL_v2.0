import os


class Config(object):
    # 日志
    LOGGER_LEVEL = "INFO"  # 日志级别
    APP_LOG_PATH = r""  # 日志存储目录
    LOG_APP_NAME = ".log"  # INFO日志
    LOG_ER_NAME = ".log"  # Error日志
    LOG_DB_NAME = '.log'

    # 应用名称
    APP_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_NAME = APP_BASE_DIR.split(os.sep)[-1]

    # IP和端口
    APP_HOST = "127.0.0.1"
    APP_PORT = "8001"

    # 数据库
    HOST = '127.0.0.1'
    PORT = 3306
    USER = 'root'
    PASSWORD = '123456'
    DB = 'app'
    CHARSET = 'utf8'
