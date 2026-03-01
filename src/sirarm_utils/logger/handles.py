import logging

from tqdm import tqdm


def color_str(*input):
    *args, string = input if len(input) > 1 else ("blue", "bold", input[0])
    colors = {
        "black": "\033[30m",  # basic colors
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",  # bright colors
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
        "end": "\033[0m",  # misc
        "bold": "\033[1m",
        "underline": "\033[4m",
    }
    return "".join(colors[x] for x in args) + f"{string}" + colors["end"]


class ColoredFormatter(logging.Formatter):
    """
    自定义日志颜色
    """
    # ANSI颜色代码
    info_color_map = {
        'DEBUG': 'cyan',  # 青色
        'INFO': 'green',  # 绿色
        'WARNING': 'yellow',  # 黄色
        'ERROR': 'red',  # 红色
        'CRITICAL': 'magenta',  # 紫色
        'RESET': 'end',
    }

    def format(self, record):
        """
        配置记录颜色
        """
        # 获取日志级别 和 消息
        origin_levelname = record.levelname
        origin_message = record.msg

        # 获取颜色
        color = self.info_color_map.get(origin_levelname, self.info_color_map['RESET'])

        # 添加颜色
        record.levelname = color_str(color, origin_levelname)
        record.msg = color_str(color, origin_message)

        # 格式化
        formatted = super().format(record)

        # 恢复日志级别 和 消息
        record.levelname = origin_levelname
        record.msg = origin_message
        return formatted


class TqdmLoggingHandle(logging.Handler):
    """
    将日志输出到tqdm.write(), 避免干扰进度条
    """

    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
            self.flush()
        except Exception:
            self.handleError(record)
            raise
