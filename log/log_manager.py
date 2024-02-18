# -*- coding: utf-8 -*-
import logging
import os

logging.basicConfig(level=logging.DEBUG)


class LogManager(object):

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
        filename = os.path.join(os.getcwd(), "log/log_files/TinyWorld.log")
        return cls._get_logger(logger_name, filename)

    @classmethod
    def get_entity_logger(cls, entity_uuid, filename):
        return cls._get_logger(entity_uuid, filename)

    @classmethod
    def get_comp_logger(cls, comp_name, filename):
        return cls._get_logger(comp_name, filename)

    @classmethod
    def get_system_logger(cls, system_name, filename):
        return cls._get_logger(system_name, filename)

    @classmethod
    def get_formatter(cls):
        return logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    @classmethod
    def get_log_file_path(cls):
        pass


# if __name__ == '__main__':
#     filename = os.path.join(os.getcwd(), "log_files/test.log")
#     if os.path.exists(filename):
#         os.remove(filename)
#     logger = LogManager.get_entity_logger("1234", filename)
#     logger.debug("debug")
#     logger.info("info")
#     logger.warning("warning")
#     logger.error("error")
#     logger.critical("critical")
