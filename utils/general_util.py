"""
General purpose utilitarian module.
"""
from datetime import timedelta


def date_range_util(start_date, end_date):
    """
    Utilitarian function that returns a date list between two given dates.
    :param date start_date: List start date.
    :param date end_date: List end date.
    :return: List of date
    """
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
