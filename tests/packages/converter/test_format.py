from src.packages.converter.format import (clean_dates, clean_days, clean_room,
                                           clean_time, convert_date, get_name,
                                           handle_meeting_patterns)


def test_get_name():
    assert (
        get_name(
            section="STAT_V 200-103 "
            "- Elementary Statistics for Applications"
        )
        == "STAT 200 103"
    )


def test_get_name_empty_string():
    assert get_name(section="") == ""


def test_get_name_break_begining():
    assert get_name(section=" -CPSC 200") == ""


def test_get_name_no_break():
    assert get_name(section="CPSC 200 201") == ""


def test_handle_meeting_patterns_3days_pm():
    assert handle_meeting_patterns(
        "2024-09-03 - 2024-12-06 |"
        " Mon Wed Fri |"
        " 2:00 p.m. - 3:00 p.m. |"
        " WESB-Floor 1-Room 100"
    ) == {
        "start_date": "20240903",
        "end_date": "20241206",
        "days": ["MO", "WE", "FR"],
        "start_time": "140000",
        "end_time": "150000",
        "room": "WESB Floor 1 Room 100",
    }


def test_handle_meeting_patterns_1day_am_pm():
    assert handle_meeting_patterns(
        mp="2024-09-05 - 2024-12-05 |"
        " Thu | 11:00 a.m. - 12:00 p.m. |"
        " ESB-Floor 1-Room 1046"
    ) == {
        "start_date": "20240905",
        "end_date": "20241205",
        "days": ["TH"],
        "start_time": "110000",
        "end_time": "120000",
        "room": "ESB Floor 1 Room 1046",
    }


def test_handle_meeting_patterns_2days_am_am():
    assert handle_meeting_patterns(
        mp="2024-09-03 - 2024-12-05 |"
        " Tue Thu | 8:00 a.m. - 9:30 a.m. |"
        " HEBB-Floor 1-Room 100"
    ) == {
        "start_date": "20240903",
        "end_date": "20241205",
        "days": ["TU", "TH"],
        "start_time": "080000",
        "end_time": "093000",
        "room": "HEBB Floor 1 Room 100",
    }


def test_clean_dates():
    assert clean_dates("2024-09-03 - 2024-12-06") == {
        "start": "20240903",
        "end": "20241206",
    }


def test_clean_days_1():
    assert clean_days("Thu") == ["TH"]


def test_clean_days_2():
    assert clean_days("Tue Sun") == ["TU", "SU"]


def test_clean_days_3():
    assert clean_days("Mon Wed Fri") == ["MO", "WE", "FR"]


def test_clean_days_invalid_day():
    assert clean_days("Mon Wed Aug") == []


def test_clean_days_empty():
    assert clean_days("") == []


def test_clean_time_am_am():
    assert clean_time("8:00 a.m. - 10:00 a.m.") == {
        "start": "080000",
        "end": "100000",
    }


def test_clean_time_am_pm():
    assert clean_time("11:00 a.m. - 1:00 p.m.") == {
        "start": "110000",
        "end": "130000",
    }


def test_clean_time_pm_pm():
    assert clean_time("2:00 p.m. - 3:00 p.m.") == {
        "start": "140000",
        "end": "150000",
    }


def test_clean_time_pm_am():  # !!! set the end day to next day
    assert clean_time("8:00 p.m. - 6:00 a.m.") == {
        "start": "200000",
        "end": "060000",
    }


def test_clean_time_invalid_time():
    assert clean_time("13:00 p.m. - 3:00 a.m.") == {
        "start": "",
        "end": "030000",
    }


def test_clean_time_invalid_time2():
    assert clean_time("6:00 a.m. - 26:00 p.m.") == {
        "start": "060000",
        "end": "",
    }


def test_clean_time_12pm_12am():  # !!! set the end day to next day
    assert clean_time("12:00 p.m. - 12:00 a.m.") == {
        "start": "120000",
        "end": "240000",
    }


def test_clean_room():
    assert clean_room("WESB-Floor 1-Room 100") == "WESB Floor 1 Room 100"


def test_convert_date():
    assert convert_date("2024-09-03") == "20240903"
