"""
Formatting utilitarian module.
"""
import platform


def path_formatter_util(path):
    """
    Utilitarian function that formats separator character in a path depending on the operating system.
    :param str path: Path to be formatted.
    :return: str
    """
    if platform.system() == 'Windows':
        return path.replace('/', '\\')
    else:
        return path.replace('\\', '/')


def request_url_formatter_util(date):
    """
    Utilitarian function that formats the request URL for data retrieval from the Costa Rica Stock Exchange.
    :param date date: Request target date
    :return: str
    """
    return f'''https://www.bolsacr.com/sites/default/files/boletines/emision/{date.strftime("%Y")}{date.strftime(
        "%m")}/{date.strftime("%Y%m%d")}.XLSX'''


def target_directory_formatter_util(start_date, end_date):
    """
    Utilitarian function that formats data harvesting target directory.
    :param date start_date: Data harvesting start date (used to name the target directory)
    :param date end_date: Data harvesting start date (used to name the target directory)
    :return: str
    """
    return f'''{start_date.strftime("%d%m%Y")}-{end_date.strftime("%d%m%Y") if int((end_date - start_date).days) > 2 else ""}'''
