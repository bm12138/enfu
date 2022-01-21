import logging


def conf_log_func():
    """日志模块配置方法"""
    # 实例化日志器
    logger = logging.getLogger()
    # 调整日志输出级别
    logger.setLevel(level=logging.INFO)
    # 实例化处理器
    sh = logging.StreamHandler()  # 输出到控制台
    # 实例化格式器
    formatter = logging.Formatter(
        fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")
    # 添加格式器给处理器
    sh.setFormatter(formatter)
    # 添加处理器给日志器
    logger.addHandler(sh)
