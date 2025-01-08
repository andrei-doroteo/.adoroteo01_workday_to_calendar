import sys

from pandas import read_excel

from src.packages.converter.transform import (
    _find_end,
    _find_start,
    import_data,
)

sys.path.append("./")

expected = read_excel("data/View_My_Courses_1.xlsx", skiprows=2)
expected2 = read_excel("data/View_My_Courses_2.xlsx", skiprows=5, skipfooter=7)
expected3 = read_excel("data/View_My_Courses_3.xlsx", skiprows=2)


def test_import_data_desktop():
    assert import_data("data/View_My_Courses_2.xlsx").equals(expected2)
    # !!! add desktop version of View_My_Courses_3.xlsx


def test_import_data_mobile():
    assert import_data("data/View_My_Courses_1.xlsx").equals(expected)
    assert import_data("data/View_My_Courses_3.xlsx").equals(expected3)


def test_find_start():
    assert _find_start("data/View_My_Courses_1.xlsx") == 2
    assert _find_start("data/View_My_Courses_2.xlsx") == 5


def test_find_end():
    assert _find_end("data/View_My_Courses_1.xlsx") == 0
    assert _find_end("data/View_My_Courses_2.xlsx") == 7
