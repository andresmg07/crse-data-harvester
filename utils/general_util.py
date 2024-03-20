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
    # Number of days between start and end date.
    date_difference = int((end_date - start_date).days)
    # If start and end date are the same, it returns start date wrapped by a
    # list.
    if date_difference < 1:
        return [start_date]
    # If there is a difference of 2 or more days between start and end date,
    # it returns the corresponding list of dates.
    for n in range(date_difference):
        yield start_date + timedelta(n)
