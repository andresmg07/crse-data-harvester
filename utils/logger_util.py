"""
Execution logger utilitarian module.
"""
import logging
from datetime import datetime
from os import getcwd, path

from utils.file_util import create_directory_util
from utils.formatter_util import path_formatter_util


def logger_setup_util(log_origin):
    """
    Utilitarian procedure that sets up the logging instrument configuration. These settings are applied across the system.
    :param log_origin: File that triggers the log.
    :return: None
    """

    log_directory_path = getcwd() + path_formatter_util("/logs/")

    if not path.exists(log_directory_path):
        create_directory_util("logs")

    log_file_path = log_directory_path + \
        str(datetime.now()).replace(":", ".") + ".log"

    with open(log_file_path, "x", encoding="utf-8"):
        logging.basicConfig(
            handlers=[
                logging.FileHandler(
                    log_file_path,
                    mode="w")],
            level=logging.INFO,
            format=f'''%(asctime)s | {log_origin} | %(levelname)s: %(message)s''',
            datefmt="%Y-%m-%d %H:%M:%S",
        )
