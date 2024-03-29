"""
Formatting utilitarian module.
"""
import platform
from datetime import timedelta


def path_formatter_util(path):
    """
    Utilitarian function that formats separator character in a path depending on the operating system.
    :param str path: Path to be formatted.
    :return: str
    """
    if platform.system() == 'Windows':
        return path.replace('/', '\\')
    return path.replace('\\', '/')


def request_url_formatter_util(date):
    """
    Utilitarian function that formats the request URL for data retrieval from the Costa Rica Stock Exchange.
    :param datetime.date date: Request target date
    :return: str
    """
    print(date)
    return f'''https://www.bolsacr.com/sites/default/files/boletines/emision/{date.strftime("%Y")}{date.strftime(
        "%m")}/{date.strftime("%Y%m%d")}.XLSX'''


def target_directory_name_formatter_util(start_date, end_date):
    """
    Utilitarian function that formats data harvesting target directory.
    :param datetime.date start_date: Data harvesting start date (used to name the target directory)
    :param datetime.date end_date: Data harvesting start date (used to name the target directory)
    :return: str
    """

    return f'''{date_string_formatter(start_date)}{"-" + date_string_formatter((end_date - timedelta(days=1))) if int((end_date - start_date).days) > 1 else ""}'''


def date_string_formatter(date):
    """
    Utilitarian function that converts date to basic formatting string.
    :param datetime.date date: Date to be converted and formatted.
    :return: str
    """
    return date.strftime("%x").replace("/", "")
