import time
import requests
from os import mkdir, chdir, getcwd, getenv
from datetime import date, datetime, timedelta
from utils.general_util import date_range_util, logging_setup, system_dependant_path_formatter
import logging
from dotenv import load_dotenv


# Function that generates the fetch URL. The response to this request is a XLSX file.
def get_fetch_url(date):
    return "https://www.bolsacr.com/sites/default/files/boletines/emision/" + date.strftime("%Y") + date.strftime(
        "%m") + '/' + date.strftime("%Y%m%d") + '.XLSX'


# Procedure that saves a file with the corresponding date as name. The files are saved in the working directory
# specified at "logging_cwd_setup" procedure
def save_file(file, date):
    open(date.strftime("%d%m%Y") + ".xlsx", "wb").write(file.content)


# Procedure that creates and changes the working directory corresponding to the date rage.
def set_target_path(start_date, end_date, is_bulk):
    target_path = system_dependant_path_formatter(getenv("SESSION_RETRIEVER_TARGET_DIRECTORY"))
    if is_bulk:
        directory_name = start_date.strftime("%d%m%Y") + "-" + end_date.strftime("%d%m%Y") if is_bulk else ""
        target_path += directory_name
        try:
            mkdir(target_path)
        except OSError as e:
            logging.error("Error creating target path for source files. " + str(e) + ".")
    try:
        chdir(target_path)
    except OSError as e:
        logging.error("Error changing to target path for source files. " + str(e) + ".")


# Main procedure, this iterates through the given dates, request and save the response files.
def retrieve_sessions_by_time_range(start_date, end_date):
    for current_date in date_range_util(start_date, end_date):
        # Avoids to request data on weekends
        if current_date.strftime("%w") not in ["0", "6"]:
            try:
                response_session_file = requests.get(get_fetch_url(current_date))
                save_file(response_session_file, current_date)
                time.sleep(0.5)
                logging.info("Trading session from " + current_date.strftime("%x") + " successfully downloaded.")
            except:
                logging.error("Couldn't retrieve session from " + current_date.strftime("%x") + ".")


# Setup procedure that configures the logging tool and change the working directory
def setup(start_date, end_date, is_bulk):
    # The logger setup below prints on console and logs file
    logging_setup(getcwd(), __file__.split("/")[-1])
    load_dotenv()
    # Creates and changes directory to the target
    set_target_path(start_date, end_date, is_bulk)


def retrieve_current_session_data(start_date, end_date):
    setup(start_date, end_date, False)
    retrieve_sessions_by_time_range(start_date, end_date)

