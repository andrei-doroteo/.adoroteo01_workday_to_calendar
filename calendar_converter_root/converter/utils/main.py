from pandas import DataFrame, read_excel
from django.core.files.uploadedfile import UploadedFile
from icalendar import Calendar

import converter.utils.manipulator as manipulator
import converter.utils.scheduling as scheduling


def import_data(file: UploadedFile) -> DataFrame:
    """ """
    data = read_excel(file, skiprows=6)[lambda df : df["Registration Status"] == "Registered"]
    
    return data


def convert_file(file: UploadedFile) -> Calendar:
    data = import_data(file)

    converted = manipulator.convert_all(data)
    data_dict = converted.to_dict(orient='records')

    # cal_name = input("Save as: ")
    return scheduling.create_ical(data_dict)


# path = input("Enter file path: ")

# convert_file(path)