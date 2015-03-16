#!/usr/bin/env python3
"""Basic logger to support other workers for github profile crawler"""

from sys import stdout
from logging import INFO, DEBUG, Formatter, getLogger, FileHandler, StreamHandler
from config import config_log_file


class BaseLogger():
    def __init__(self, level=INFO):
        log_formatter = Formatter("%(asctime)s [%(module)s][%(process)d][%(levelname)s] %(message)s")
        self._root_logger = getLogger()
        self._root_logger.setLevel(level)
        self._root_logger.addHandler(self._file_handler(log_formatter))
        self._root_logger.addHandler(self._console_handler(log_formatter))


    def _file_handler(self, log_formatter):
        file_handler = FileHandler(config_log_file)
        file_handler.setFormatter(log_formatter)
        return file_handler


    def _console_handler(self, log_formatter):
        console_handler = StreamHandler(stdout)
        console_handler.setFormatter(log_formatter)
        return console_handler


    def _log_critical(self, msg, *args, **kwargs):
        self._root_logger.critical(msg, *args, **kwargs)


    def _log_error(self, msg, *args, **kwargs):
        self._root_logger.error(msg, *args, **kwargs)


    def _log_exception(self, msg, *args, **kwargs):
        self._root_logger.exception("Exception: {}".format(msg, *args, **kwargs))


    def _log_warning(self, msg, *args, **kwargs):
        self._root_logger.warning(msg, *args, **kwargs)


    def _log_info(self, msg, *args, **kwargs):
        self._root_logger.info(msg, *args, **kwargs)


    def _log_debug(self, msg, *args, **kwargs):
        self._root_logger.debug(msg, *args, **kwargs)


class Example(BaseLogger):
    def __init__(self):
        BaseLogger.__init__(self, DEBUG)


    def process(self):
        self._log_critical("hello critical %s", "yes!")
        self._log_error("hello error")
        try:
            x = 5 / 0
        except Exception as e:
            self._log_exception("hello exception %s", "oops!")
        self._log_warning("hello warning")
        self._log_info("hello info - hao%d", 123)
        self._log_debug("hello debug")


def main():
    ex = Example()
    ex.process()


if __name__ == '__main__':
    main()
