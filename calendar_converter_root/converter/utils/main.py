import converter.utils.manipulator as manipulator
import converter.utils.scheduling as scheduling
from django.core.files.uploadedfile import UploadedFile
from icalendar import Calendar
from pandas import DataFrame


def import_data(file: UploadedFile) -> DataFrame:
    """ """

    def find_start(file: UploadedFile) -> int:
        # TODO
        """
        Inputs:
        - file
            - a file upload of a UBC workday class schedule

        Returns:
        - an int of the index of the begining row of (the column names)
        the schedule data

        """

        return 0  # stub

    def find_end(file: UploadedFile) -> int:
        # TODO:
        """
        Inputs:
        - file
            - a file upload of a UBC workday class schedule

        Returns:
        - an int of the index of the ending row of the schedule data
        (the last enrolled course)

        """

        return 0  # stub

    def get_data(file: UploadedFile, start: int, end: int) -> DataFrame:
        # TODO:
        """
        Inputs:
        - file
            - a file upload of a UBC workday class schedule

        Returns:
        - an int of the index of the ending row of the schedule data
        (the last enrolled course)

        """

        return DataFrame({})  # stub

    start = find_start(file)
    end = find_end(file)

    data = get_data(file, start, end)

    return data


def convert_file(file: UploadedFile) -> Calendar:
    data = import_data(file)

    converted = manipulator.convert_all(data)
    data_dict = converted.to_dict(orient="records")

    # cal_name = input("Save as: ")
    return scheduling.create_ical(data_dict)


# path = input("Enter file path: ")

# convert_file(path)
