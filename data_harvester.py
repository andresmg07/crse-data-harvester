import logging
import time
from os import mkdir, getcwd

import requests

from utils.file_util import save_excel_file_util
from utils.formatter_util import request_url_formatter_util, target_directory_formatter_util
from utils.general_util import date_range_util
from utils.logger_util import logger_setup_util


# Procedure that creates and changes the working directory corresponding
# to the date rage.
def create_target_path(start_date, end_date, base_path):
    target_directory_name = target_directory_formatter_util(
        start_date, end_date)
    target_path = base_path + target_directory_name
    try:
        mkdir(target_path)
        return target_path
    except OSError as e:
        logging.error(
            "Error creating target path for data harvest result files. %s.",
            str(e))


# Main procedure, this iterates through the given dates, request and save
# the response files.
def harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path):
    for date in date_range_util(start_date, end_date):

        session_data_file = None
        # Avoids to request data on weekends
        if date.strftime("%w") not in ["0", "6"]:
            try:
                session_data_file = requests.get(
                    request_url_formatter_util(date), timeout=5)
            except requests.exceptions.RequestException as e:
                logging.error(
                    "Couldn't retrieve session from %s. Detailed error: %s", date.strftime("%x"), e)
            save_excel_file_util(
                harvest_target_directory_path,
                date.strftime("%x"),
                session_data_file.content)
            time.sleep(0.5)
            logging.info(
                "Trading session from %s successfully downloaded.",
                date.strftime("%x"))


def data_harvester(start_date, end_date, base_path):
    # The logger setup below prints on console and log file
    logger_setup_util(getcwd(), __file__.rsplit('/', maxsplit=1)[-1])
    # Creates and changes directory to the target
    harvest_target_directory_path = create_target_path(
        start_date, end_date, base_path)
    harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path)
