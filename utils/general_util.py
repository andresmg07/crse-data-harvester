"""
General purpose utilitarian module.
"""
from datetime import timedelta


def date_range_util(start_date, end_date):
    """
    Utilitarian function that returns a date list between two given dates.
    :param datetime.date start_date: List start date.
    :param datetime.date end_date: List end date.
    :return: List of date
    """
    date_difference = int((end_date - start_date).days)
    if date_difference < 1:
        return [start_date]
    for n in range(date_difference):
        yield start_date + timedelta(n)
