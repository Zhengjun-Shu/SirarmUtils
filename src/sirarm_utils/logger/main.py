import logging

from .handles import TqdmLoggingHandle, ColoredFormatter

LoggerCenter = {}

class LoggerManager:
    _log_format = "%(asctime)s - [%(name)s] - [%(filename)s:%(funcName)s:%(lineno)d] - %(levelname)s |>: %(message)s"
    _date_format = "%Y-%m-%d %H:%M:%S"

    def get_logger(
            self,
            name: str = __name__,
            level=logging.INFO,
    ) -> logging.Logger:
        if name in LoggerCenter:
            return LoggerCenter[name]
        # 创建 logger
        logger = logging.getLogger(name)
        # 配置日志等级
        logger.setLevel(level)
        # 如果 logger 已经有处理器，则直接返回
        if not logger.handlers:
            console_handler = TqdmLoggingHandle()
            console_handler.setLevel(level)
            console_handler.setFormatter(ColoredFormatter(self._log_format, datefmt=self._date_format))
            logger.addHandler(console_handler)
        LoggerCenter[name] = logger
        return logger


class LoggerLevel:
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


def setup_logger(
        name: str = __name__,
        default_level: str = LoggerLevel.INFO
) -> logging.Logger:
    log_level_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    return LoggerManager().get_logger(name, log_level_map[default_level])
