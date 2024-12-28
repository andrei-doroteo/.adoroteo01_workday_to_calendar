from django.core.files.uploadedfile import UploadedFile
from icalendar import Calendar
from pandas import DataFrame

from .calendar import create_ical
from .data import convert_all


def import_data(file: UploadedFile) -> DataFrame:
    """
    Inputs:
    - file: a file upload of a UBC workday class schedule

    Returns:
    - a Dataframe of the schdeule content of the uploaded UBC workday
    schedule
    """

    start = _find_start(file)
    end = _find_end(file)

    data = _get_data(file, start, end)

    return data


def _find_start(file: UploadedFile) -> int:
    # TODO
    """
    Inputs:
    - file: a file upload of a UBC workday class schedule

    Returns:
    - an int of the index of the begining row of (the column names)
    the schedule data

    """

    return 0  # stub


def _find_end(file: UploadedFile) -> int:
    # TODO:
    """
    Inputs:
    - file: a file upload of a UBC workday class schedule

    Returns:
    - an int of the index of the ending row of the schedule data
    (the last enrolled course)

    """

    return 0  # stub


def _get_data(file: UploadedFile, start: int, end: int) -> DataFrame:
    # TODO:
    """
    Inputs:
    - file: a file upload of a UBC workday class schedule

    Returns:
    - a dataframe of file's

    """

    return DataFrame({})  # stub


def convert_file(file: UploadedFile) -> Calendar:
    data = import_data(file)

    converted = convert_all(data)
    data_dict = converted.to_dict(orient="records")

    return create_ical(data_dict)
