"""
File and directory manipulation utilitarian module.
"""
import logging
import warnings
from os import mkdir, getcwd

from pandas import read_excel


def load_excel_file_util(file_path, initial_rows_skip_range=0):
    """
    Utilitarian function that loads into memory a panda's dataframe from an Excel file.
    :param str file_path: Source file path.
    :param int or None initial_rows_skip_range: Number of rows to skip at the beginning of the document.
    :return: pandas.DataFrame
    """
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        return read_excel(
            file_path,
            skiprows=initial_rows_skip_range,
            engine="openpyxl")


def save_excel_file_util(directory_path, file_name, content):
    """
    Utilitarian procedure that saves into disk an Excel file.
    :param str directory_path: Target directory path.
    :param str file_name: Target file name.
    :param bytes content: Contents to be saved into target file.
    :return: None
    """
    with open(f'''{directory_path}/{file_name}.xlsx''', "wb") as excel_file:
        excel_file.write(content)


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
            "Error creating directory. Detailed error: %s.",
            str(e))
    return target_path
