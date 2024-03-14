from datetime import timedelta, datetime
import logging
import os
import warnings
from pandas import read_excel
import platform


# Utilitarian function that returns a group of dates inside the range given to iterate.
def date_range_util(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# Utilitarian function that sets up the logging instrument configuration. These settings are applied across the system.
def logging_setup(main_directory, log_origin):
    log_file_path = main_directory + system_dependant_path_formatter("/logs/retriever/") + str(datetime.now()).replace(
        ":", ".") + ".log"

    open(log_file_path, "x")

    logging.basicConfig(
        handlers=[logging.FileHandler(log_file_path, mode="w")],
        level=logging.DEBUG,
        format="%(asctime)s - " + log_origin + " - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# Utilitarian function that returns formatted date from source file name.
def get_date_from_session_file_name(file_name):
    formatted_file_name = file_name.replace(".xlsx", "")
    return datetime.strptime(formatted_file_name, "%d%m%Y").strftime("%Y-%m-%d")


# Utilitarian function that sort file list by name (date). This function ignores hidden and temp files.
def get_sorted_session_files(file_list):
    filtered_file_list = [file for file in file_list if not file.startswith('.') and not file.startswith('~')]
    return sorted(
        filtered_file_list,
        key=lambda x: datetime.strptime(x.replace(".xlsx", ""), '%d%m%Y'))


# Utilitarian function that loads a panda's dataframe from file path. It receives a number of rows to skip from the
# beginning of the file, this to avoid unnecessary data. This function also normalizes column headers.
def load_data_frame_from_excel(file_path, initial_rows_skip_range):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        file = read_excel(file_path, skiprows=initial_rows_skip_range, engine="openpyxl")
        accent_removed_headers = file.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode(
            'utf-8')
        normalized_headers = [header.lower() for header in accent_removed_headers]
        file.columns = normalized_headers
        return file


# Utilitarian function that formats separator character in path depending on operating system.
def system_dependant_path_formatter(path):
    if platform.system() == 'Windows':
        return path.replace('/', '\\')
    else:
        return path.replace('\\', '/')


# Utilitarian function that removes all files in a given path.
def remove_all_files(path):
    try:
        target_path = system_dependant_path_formatter(path)
        filelist = [f for f in os.listdir(target_path)]
        for f in filelist:
            os.remove(os.path.join(target_path, f))
    except OSError as e:
        logging.error("Error changing to target path for source files. " + str(e) + ".")
