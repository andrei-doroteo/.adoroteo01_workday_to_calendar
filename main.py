from pandas import DataFrame, read_excel

import manipulator
import scheduling


def import_data(file: str) -> DataFrame:
    """ """
    data = read_excel(file, skiprows=2)
    return data


def convert_file(file: str) -> None:
    data = import_data(file)

    converted = manipulator.convert_all(data)
    data_dict = converted.to_dict(orient='records')

    cal_name = input("Save as: ")
    scheduling.create_ical(data_dict,cal_name + ".ics")


path = input("Enter file path: ")

convert_file(path)