# -*- coding: utf-8 -*-
import logging
import os

logging.basicConfig(level=logging.DEBUG)


class LogManager(object):
    WORLD_LOG = "log/log_files/TinyWorld.log"
    DEBUG_LOG = "log/log_files/Debug.log"

    @classmethod
    def clear_logs(cls):
        for log_file in [cls.WORLD_LOG, cls.DEBUG_LOG]:
            filename = os.path.join(os.getcwd(), log_file)
            with open(filename, 'w') as file:
                file.truncate(0)

    @classmethod
    def _get_logger(cls, logger_name, filename=None):
        logger = logging.getLogger(logger_name)
        if filename:
            file_handler = logging.FileHandler(filename)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(cls.get_formatter())
            logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(cls.get_formatter())
        logger.addHandler(console_handler)
        logger.propagate = False
        return logger

    @classmethod
    def get_world_logger(cls):
        logger_name = "TinyWorld"
        filename = os.path.join(os.getcwd(), cls.WORLD_LOG)
        cls.check_filename_exists(filename)
        return cls._get_logger(logger_name, filename)

    @classmethod
    def get_debug_logger(cls, logger_name):
        filename = os.path.join(os.getcwd(), cls.DEBUG_LOG)
        cls.check_filename_exists(filename)
        return cls._get_logger(logger_name, filename)

    @classmethod
    def get_formatter(cls):
        return logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    @classmethod
    def get_log_file_path(cls):
        pass

    @classmethod
    def check_filename_exists(cls, filename):
        if not os.path.exists(filename):
            os.makedirs(os.path.dirname(filename))
            with open(filename, "w") as f:
                pass


# just for test
# if __name__ == '__main__':
#     filename = os.path.join(os.getcwd(), "log_files/test.log")
#     if os.path.exists(filename):
#         os.remove(filename)
#     logger = LogManager.get_debug_logger("1234", filename)
#     logger.debug("debug")
#     logger.info("info")
#     logger.warning("warning")
#     logger.error("error")
#     logger.critical("critical")
