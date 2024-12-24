import sys
sys.path.append("./")
from ..main import *

expected = read_excel('data/View_My_Courses_1.xlsx', skiprows=3)


def test_import_data_desktop():
    assert import_data('data/View_My_Courses_1.xlsx').equals(expected)


def test_import_data_mobile():
    assert import_data('data/View_My_Courses.xlsx').equals(expected)