import sys

from pandas import read_excel

from src.packages.converter.transform import import_data, _find_start, _find_end

sys.path.append("./")

expected = read_excel("data/View_My_Courses_1.xlsx", skiprows=2)


def test_import_data_desktop():
    assert import_data("data/View_My_Courses_1.xlsx").equals(expected)


def test_import_data_mobile():
    assert import_data("data/View_My_Courses.xlsx").equals(expected)


def test_find_start():
    assert _find_start("data/View_My_Courses_1.xlsx") == 2
    assert _find_start("data/View_My_Courses_2.xlsx") == 5


def test_find_end():
    assert _find_end("data/View_My_Courses_1.xlsx") == 0
    assert _find_end("data/View_My_Courses_2.xlsx") == 7
