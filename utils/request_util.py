import requests


def get_request(url, timeout=5):
    harvested_data_file = requests.get(url, timeout=timeout)
    harvested_data_file.raise_for_status()
    return harvested_data_file.content
