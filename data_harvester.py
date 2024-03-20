"""
BNV trading session data harvester main module.
"""
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


def harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path):
    """

    :param datetime.date start_date: Harvesting start date.
    :param datetime.date end_date: Harvesting end date (exclusive).
    :param harvest_target_directory_path:
    :return: None
    """
    for target_date in date_range_util(start_date, end_date):
        # This control structure avoids requesting data on weekends.
        if target_date.strftime("%w") not in ["0", "6"]:
            try:
                # Requests trading session data file.
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
            # Normalize retrieved trading session data file.
            normalized_harvested_data_file = data_normalizer(
                harvested_data_file)
            # Save on disk normalized trading session data file.
            save_dataframe_as_excel_file_util(
                harvest_target_directory_path,
                date_string_formatter(target_date),
                normalized_harvested_data_file)
            # Passive waiting to avoid server overload.
            time.sleep(0.25)
            logging.info(
                "Trading session from %s successfully harvested.",
                target_date.strftime("%x"))


def data_harvester_setup(start_date, end_date):
    """
    Auxiliary function that sets up the harvester.
    This function is in charge of initializing the logger and creates target directories.
    :param datetime.date start_date: Harvesting start date.
    :param datetime.date end_date: Harvesting end date (exclusive).
    :return: str
    """

    # Logger setup call.
    logger_setup_util(__file__.rsplit('/', maxsplit=1)[-1])

    # Required directories definition.
    harvest_result_directory_path = getcwd() + "/harvest_result/"
    harvest_target_directory_name = target_directory_name_formatter_util(
        start_date, end_date)
    harvest_target_directory_path = harvest_result_directory_path + \
        harvest_target_directory_name

    # Checks if required directories exist, if not it creates them.
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
    """
    Modules main procedure.
    Harvest trading session data from the BNV web service within a date range.
    Note: This procedure will harvest trading session data from the start date till the end date minus one day.
    :param datetime.date start_date: Harvesting start date.
    :param datetime.date end_date: Harvesting end date (exclusive).
    :return: None
    """
    # Directory where trading session data files will be stored once harvested.
    harvest_target_directory_path = data_harvester_setup(start_date, end_date)
    harvest_data_by_time_range(
        start_date,
        end_date,
        harvest_target_directory_path)


data_harvester(date(2024, 1, 1), date(2024, 1, 4))
