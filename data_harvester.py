import logging
import time
from datetime import date
from os import path, getcwd

import requests

from data_normalizer import data_normalizer
from utils.file_util import create_directory_util, save_dataframe_as_excel_file_util
from utils.formatter_util import request_url_formatter_util, target_directory_name_formatter_util, date_string_formatter
from utils.general_util import date_range_util
from utils.logger_util import logger_setup_util
from utils.request_util import get_request


# Main procedure, this iterates through the given dates, request and save
# the response files.
def harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path):
    for target_date in date_range_util(start_date, end_date):
        # Avoids to request data on weekends
        if target_date.strftime("%w") not in ["0", "6"]:
            try:
                harvested_data_file = get_request(
                    request_url_formatter_util(target_date))
                logging.info(
                    "Trading session file from %s successfully retrieved.",
                    target_date.strftime("%x"))
            except requests.exceptions.RequestException as e:
                logging.error(
                    "Couldn't retrieve session from %s. %s",
                    target_date.strftime("%x"),
                    e)
                continue
            normalized_harvested_data_file = data_normalizer(
                harvested_data_file)
            save_dataframe_as_excel_file_util(
                harvest_target_directory_path,
                date_string_formatter(target_date),
                normalized_harvested_data_file)
            time.sleep(0.5)
            logging.info(
                "Trading session from %s successfully harvested.",
                target_date.strftime("%x"))


def data_harvester_setup(start_date, end_date):
    logger_setup_util(__file__.rsplit('/', maxsplit=1)[-1])

    harvest_result_directory_path = getcwd() + "/harvest_result/"
    harvest_target_directory_name = target_directory_name_formatter_util(
        start_date, end_date)
    harvest_target_directory_path = harvest_result_directory_path + \
        harvest_target_directory_name

    if not path.exists(harvest_result_directory_path):
        create_directory_util(
            harvest_target_directory_name,
            create_directory_util("harvest_result"))
    else:
        if not path.exists(harvest_target_directory_path):
            create_directory_util(
                harvest_target_directory_name,
                harvest_result_directory_path)

    return harvest_target_directory_path


def data_harvester(start_date, end_date):
    harvest_target_directory_path = data_harvester_setup(start_date, end_date)
    harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path)


data_harvester(date(2024, 1, 1), date(2024, 1, 4))
