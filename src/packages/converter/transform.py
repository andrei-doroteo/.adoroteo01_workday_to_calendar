from django.core.files.uploadedfile import UploadedFile
from icalendar import Calendar
from pandas import DataFrame, read_excel

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

    return read_excel(file, skiprows=start, skipfooter=end)


def _find_start(file: UploadedFile) -> int:
    # TODO
    """
    Inputs:
    - file: a file upload of a UBC workday class schedule

    Returns:
    - an int of the index of the begining row of (the column names)
    the schedule data

    """

    data = read_excel(file, header=None)

    def _get_row_with_header() -> DataFrame:
        """
        Returns dataframe of row(s) in data that match the header row,
        keeping the same index values as data
        """
        header = (
            (data[0].isna())
            & (data[1] == "Course Listing")
            & (data[2] == "Credits")
            & (data[3] == "Grading Basis")
            & (data[4] == "Section")
            & (data[5] == "Instructional Format")
            & (data[6] == "Delivery Mode")
            & (data[7] == "Meeting Patterns")
            & (data[8] == "Registration Status")
            & (data[9] == "Instructor")
            & (data[10] == "Start Date")
            & (data[11] == "End Date")
        )
        return data[header]

    def _get_index_of_header() -> int:
        """
        Returns the index of the first row in data that contains all the
        column names
        """
        return _get_row_with_header().index[0]

    return _get_index_of_header()


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


def convert_file(file: UploadedFile) -> Calendar:
    data = import_data(file)

    converted = convert_all(data)
    data_dict = converted.to_dict(orient="records")

    return create_ical(data_dict)
