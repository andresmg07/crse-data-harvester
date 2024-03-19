"""
Harvested data normalization module.
"""

from utils.file_util import load_excel_file_as_dataframe_util


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
    # Removes accents.
    data_frame.columns = data_frame.columns.str.strip().str.lower().str.replace(
        " - ",
        "_").str.replace(
        " ",
        "_").str.normalize('NFKD').str.encode(
            'ascii',
        errors='ignore').str.decode('utf-8')
    data_frame = data_frame.applymap(
        lambda s: s.lower().strip() if isinstance(s, str) else s)
    return data_frame


def normalize_usable_columns(data_frame):
    return data_frame[[
        "isin",
        "serie",
        "fecha_vencimiento",
        "pais_emisor",
        "moneda",
        "emisor",
        "tasa",
        "precio_vector",
        "rendimiento_vector",
        "recomprable",
        "instrumento",
        "periodicidad",
        "premio",
        "tipo_emision",
        "monto_aprobado",
        "monto_colocado",
        "estado",
        "oficial",
        "garantia_cumplimiento",
        "garantia_margen",
        "precio_moneda_vector",
        "precio_minimo",
        "castigo",
        "precio_ajustado",
        "bursatilidad_vigente",
        "bursatilidad_del_dia",
        "facial_abierto",
    ]]


def normalize_boolean_data_points(data_frame):
    data_frame["estado"] = data_frame["estado"].apply(
        lambda x: x == "a")
    data_frame["oficial"] = data_frame["oficial"].apply(
        lambda x: x == "si")
    data_frame["recomprable"] = data_frame["recomprable"].apply(
        lambda x: x == "si")


def normalize_level_data_points(data_frame):
    data_frame["bursatilidad_del_dia"] = data_frame["bursatilidad_del_dia"].apply(normalize_level_data_point)
    data_frame["bursatilidad_vigente"] = data_frame["bursatilidad_vigente"].apply(normalize_level_data_point)


def data_normalizer(harvested_data_file):
    data_frame = load_excel_file_as_dataframe_util(harvested_data_file, 5)
    data_frame = normalize_data_format(data_frame)
    data_frame = normalize_usable_columns(data_frame)
    normalize_boolean_data_points(data_frame)
    normalize_level_data_points(data_frame)
    return data_frame
