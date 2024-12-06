import logging
import os
from datetime import datetime

# 创建日志记录器
def setup_logger(log_file_name="app.log", level=logging.DEBUG):
    """
    设置日志记录器。

    :param log_file_name: 日志文件名，默认 "app.log"
    :param level: 日志级别，默认 DEBUG
    :return: 配置好的日志记录器
    """
    # 确保日志目录存在
    log_dir = "../../logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 创建日志文件路径
    log_file_path = os.path.join(log_dir, log_file_name)

    # 格式化日志信息
    log_format = (
        "%(asctime)s - [%(levelname)s] - "
        "%(filename)s:%(lineno)d - %(message)s"
    )
    date_format = "%Y-%m-%d %H:%M:%S"

    # 创建日志记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # 创建文件处理器
    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setLevel(level)

    # 设置格式
    formatter = logging.Formatter(log_format, datefmt=date_format)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 添加处理器到记录器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# 初始化日志记录器
logger = setup_logger()

# 测试日志
if __name__ == "__main__":
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
