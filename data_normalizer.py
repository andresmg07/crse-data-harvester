"""
Harvested data normalization module.
"""


def normalize_headers(data_frame):
    """
    Normalization procedure that removes unwanted characters from column headers.
    :param pandas.dataframe data_frame: Data frame to be normalized.
    :return: None
    """
    accent_removed_headers = data_frame.columns.str.normalize(
        'NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    normalized_headers = [header.lower() for header in accent_removed_headers]
    data_frame.columns = normalized_headers
