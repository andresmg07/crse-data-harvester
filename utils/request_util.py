"""
HTTP request utilitarian module.
"""
import requests


def get_request(url, timeout=5):
    """
    HTTP GET request utilitarian function
    :param str url: Target URL to HTTP GET request.
    :param int or none timeout: Request timeout in seconds.
    :return: bytes
    """
    harvested_data_file = requests.get(url, timeout=timeout)
    harvested_data_file.raise_for_status()
    return harvested_data_file.content
