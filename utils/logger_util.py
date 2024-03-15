"""
Execution logger utilitarian module.
"""
import logging
from datetime import datetime
from utils.formatter_util import path_formatter_util


def logger_setup_util(main_directory, log_origin):
    """
    Utilitarian procedure that sets up the logging instrument configuration. These settings are applied across the system.
    :param main_directory: Main directory of the project.
    :param log_origin: File that triggers the log.
    :return: None
    """
    log_file_path = main_directory + path_formatter_util("/logs/") + str(datetime.now()).replace(
        ":", ".") + ".log"

    open(log_file_path, "x")

    logging.basicConfig(
        handlers=[logging.FileHandler(log_file_path, mode="w")],
        level=logging.DEBUG,
        format="%(asctime)s - " + log_origin + " - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
