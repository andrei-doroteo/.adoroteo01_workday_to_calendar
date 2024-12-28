# Andrei Doroteo
# 2024/08/17
#
# This module handles the manipulation of schedule data, including
# the application of the conversion functions

from copy import deepcopy

from pandas import DataFrame

from .format import get_name, handle_meeting_patterns


def convert_all(data: DataFrame) -> DataFrame:
    """
    ## Inputs
    - data
        - A dataframe of a UBC workdayschedule

        **for example:** this [excel sheet][1] if it
        was converted to a DataFrame with pandas.read_excel()

    ## Returns
    - A dataframe of converted courses
    for ease of use

    keeps only the Section and Meeeting Patterns
    columns in the schedule and converts
    them into the desired format

    [1]: (https://github.com/Adoroteo01/.adoroteo01_workday_to_calendar/
    blob/main/data/View_My_Courses.xlsx)
    """

    def filter_data(data: DataFrame) -> DataFrame:

        data_filtered = data[["Section", "Meeting Patterns"]]
        return data_filtered

    def remove_missing_values(data: DataFrame) -> DataFrame:

        data_cleaned = data.dropna()
        return data_cleaned

    def to_dict(data: DataFrame) -> list[dict]:

        data_dict = data.to_dict(orient="records")
        return data_dict

    def to_dataframe(dicts: list[dict]) -> DataFrame:

        dict_as_dataframe = DataFrame(dicts)
        return dict_as_dataframe

    filtered = filter_data(data)

    cleaned = remove_missing_values(filtered)

    data_dict = to_dict(cleaned)

    split = split_meeting_patterns(data_dict)

    data_df = to_dataframe(split)

    convert_cols(data_df)

    return data_df


def split_meeting_patterns(schedule: list[dict]) -> list[dict]:
    """
    ## Inputs
    - schedule
        - a list of dicts where each dict represents a row of a
        DataFrame. This list of dicts must have been obtained from
        a UBC workday schedule DataFrame. (see line 15)

    ## Returns
    - a list of dicts with 2 dicts in place of any entry wuth 2 meeting
    patterns

    turns each dict with 2 entries in the 'Meeting Patterns' collumn
    into 2 seperate dicts with 1 entry in the 'Meeting Patterns'\
    collumn.

    split dicts are put in the same spot they were in the list.
    """

    def merge_lists(lol: list[list[dict]], merged: list[dict]) -> list[dict]:
        """
        merges a 2d list into 1 list
        """

        if lol == []:
            return merged

        else:
            return merge_lists(lol=lol[1:], merged=merged + lol[0])

    all_meeting_patterns_split = list(map(split_course, schedule))

    merged_lists = merge_lists(lol=all_meeting_patterns_split)

    return merged_lists  # merged_lists


def split_course(course: dict) -> list[dict]:
    """
    ## Inputs
    - course
        - a dict with keys equivalent to the columns of a UBC worday
        schedule (see line 15)

    ## Returns
    - either a list of 1 dict or list of 2 dict depending on
    if it has 2 meeting patters

    if dict has 2 meeting patterns, produces a list of 2
    dicts with 1 meeting pattern each.

    if dict has 1 meeting pattern there will be 1 dict
    in the list.
    """

    # {"Meeting Patterns":"m - p - 1\n\nm - p - 2"}

    def has_two_meeting_patterns(course: dict) -> bool:
        return "\n\n" in course["Meeting Patterns"]

    if has_two_meeting_patterns(course):

        lom = course["Meeting Patterns"].split("\n\n")

        meeting_pattern1 = lom[0]
        meeting_pattern2 = lom[1]

        new_entry1 = deepcopy(course)
        new_entry1["Meeting Patterns"] = meeting_pattern1

        new_entry2 = deepcopy(course)
        new_entry2["Meeting Patterns"] = meeting_pattern2

        # list of entries
        return [new_entry1, new_entry2]

    else:
        return [course]


# TODO: implement
def convert_cols(data: DataFrame) -> None:
    """
    ## Inputs
    - data
        - the DataFrame obtained after splitting the meeting patterns
        with split_meeting_patterns()

    ## Returns
    - None

    converts the 'Section' and 'Meeting Patterns' collumn into the
    format specified in data.py
    """

    # TODO: implement
    def convert_sections(data: DataFrame) -> None:
        """ """

        data["Section"] = data["Section"].apply(get_name)

    # TODO: implement
    def convert_meeting_patterns(data: DataFrame) -> None:
        """ """

        data["Meeting Patterns"] = (
            data["Meeting Patterns"].astype(str).apply(handle_meeting_patterns)
        )

    convert_sections(data)

    convert_meeting_patterns(data)
