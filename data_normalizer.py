"""
Harvested data normalization module.
"""
import numpy as np
from pandas import Timestamp


def normalize_level_data_point(level_data_point):
    match level_data_point:
        case "minima":
            return 0
        case "baja":
            return 1
        case "media":
            return 2
        case "alta":
            return 3
        case _:
            return None


def normalize_boolean_data_point(boolean_data_point, truth_value):
    return boolean_data_point == truth_value


def normalize_data_format(data_frame):
    # Format empty data points.
    data_frame.replace(np.nan, None)
    # Format date data points.
    data_frame.replace(Timestamp, lambda data_point: data_point.strftime("%Y-%m-%d"))
    # Removes accents.
    data_frame.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    # Remove leading or trailing whitespace and transform to lower cases.
    data_frame.str.strip().str.lower()


def data_normalizer(data_frame):
    normalize_data_format(data_frame)