"""
File and directory manipulation utilitarian module.
"""
import logging
import warnings
from os import mkdir, getcwd

from pandas import read_excel


def load_excel_file_as_dataframe_util(excel_source, initial_rows_skip_range=0):
    """
    Utilitarian function that loads into memory a panda's dataframe from an Excel file.
    :param str or bytes excel_source: Source file.
    :param int or None initial_rows_skip_range: Number of rows to skip at the beginning of the document.
    :return: pandas.DataFrame
    """
    try:
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            return read_excel(
                excel_source,
                index_col=0,
                skiprows=initial_rows_skip_range,
                engine="openpyxl")
    except OSError as e:
        logging.error(
            "Error loading into pandas dataframe excel file. %s.",
            str(e))
        return None


def save_dataframe_as_excel_file_util(directory_path, file_name, data_frame):
    """
    Utilitarian procedure that saves into disk an Excel file.
    :param str directory_path: Target directory path.
    :param str file_name: Target file name.
    :param pandas.DataFrame data_frame: Contents to be saved into target file.
    :return: None
    """
    try:
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            data_frame.to_csv(
                f'''{directory_path}/{file_name}.csv''',
                index=False)
    except OSError as e:
        logging.error(
            "Error saving data frame into excel file. %s.",
            str(e))


def create_directory_util(directory_name, base_path=getcwd()):
    """
    Utilitarian function that creates a directory.
    :param str directory_name: Name of the directory to be created.
    :param str or None base_path:
    :return: str
    """
    target_path = f'''{base_path}/{directory_name}'''
    try:
        mkdir(target_path)
    except OSError as e:
        logging.error(
            "Error creating directory. %s.",
            str(e))
    return target_path
