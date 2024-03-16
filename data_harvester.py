import logging
import time
from datetime import date
from os import path, getcwd

import requests

from utils.file_util import save_excel_file_util, create_directory_util
from utils.formatter_util import request_url_formatter_util, target_directory_name_formatter_util
from utils.general_util import date_range_util
from utils.logger_util import logger_setup_util


# Main procedure, this iterates through the given dates, request and save
# the response files.
def harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path):
    for target_date in date_range_util(start_date, end_date):
        print(target_date)
        session_data_file = None
        # Avoids to request data on weekends
        if target_date.strftime("%w") not in ["0", "6"]:
            try:
                session_data_file = requests.get(
                    request_url_formatter_util(target_date), timeout=5)
            except requests.exceptions.RequestException as e:
                logging.error(
                    "Couldn't retrieve session from %s. Detailed error: %s",
                    target_date.strftime("%x"),
                    e)
            save_excel_file_util(
                harvest_target_directory_path,
                target_date.strftime("%x").replace("/", ""),
                session_data_file.content)
            time.sleep(0.5)
            logging.info(
                "Trading session from %s successfully downloaded.",
                target_date.strftime("%x"))


def data_harvester_setup(start_date, end_date):
    logger_setup_util(__file__.rsplit('/', maxsplit=1)[-1])

    harvest_result_directory_path = getcwd() + "/harvest_result/"
    harvest_target_directory_name = target_directory_name_formatter_util(start_date, end_date)
    harvest_target_directory_path = harvest_result_directory_path + harvest_target_directory_name

    if not path.exists(harvest_result_directory_path):
        create_directory_util(harvest_target_directory_name, create_directory_util("harvesting_result"))
    else:
        if not path.exists(harvest_target_directory_path):
            create_directory_util(harvest_target_directory_name)

    return harvest_target_directory_path


def data_harvester(start_date, end_date):
    harvest_target_directory_path = data_harvester_setup(start_date, end_date)
    print(harvest_target_directory_path)
    harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path)


data_harvester(date(2024, 2, 2), date(2024, 2, 3))
