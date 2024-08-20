import sys
sys.path.append("./")
import info

### get_name() tests

def test_get_name():
    assert info.get_name(section="STAT_V 200-103 "
                         "- Elementary Statistics for Applications") \
                            == "STAT 200 103"

def test_get_name_empty_string():
    assert info.get_name(section="") == ""

def test_get_name_break_begining():
    assert info.get_name(section=" -CPSC 200") == ""

def test_get_name_no_break():
    assert info.get_name(section="CPSC 200 201") == ""


### handle_meeting_patterns() tests !!!

def test_handle_meeting_patterns_3days_pm():
    assert info.handle_meeting_patterns("mp=2024-09-03 - 2024-12-06 |"
                                        " Mon Wed Fri |"
                                        " 2:00 p.m. - 3:00 p.m. |"
                                        " WESB-Floor 1-Room 100") \
    == {"days":["MO", "WE", "FR"],
        "start_time":"140000",
        "end_time":"150000",
        "room":"WESB Floor 1 Room 100"}

def test_handle_meeting_patterns_1day_am_pm():
    assert info.handle_meeting_patterns(mp="2024-09-05 - 2024-12-05 |"
                                        " Thu | 11:00 a.m. - 12:00 p.m. |"
                                        " ESB-Floor 1-Room 1046") \
    == {"days":["TH"],
        "start_time":"110000",
        "end_time":"120000",
        "room":"ESB Floor 1 Room 1046"}

def test_handle_meeting_patterns_2days_am_am():
    assert info.handle_meeting_patterns(mp="2024-09-03 - 2024-12-05 |"
                                        " Tue Thu | 8:00 a.m. - 9:30 a.m. |"
                                        " HEBB-Floor 1-Room 100") \
    == {"days":["TU", "TH"],
        "start_time":"080000",
        "end_time":"093000",
        "room":"HEBB Floor 1 Room 100"}



### clean_days() tests

def test_clean_days_1():
    assert info.clean_days("Thu") == ["TH"]

def test_clean_days_2():
    assert info.clean_days("Tue Sun") == ["TU", "SU"]

def test_clean_days_3():
    assert info.clean_days("Mon Wed Fri") == ["MO", "WE", "FR"]

def test_clean_days_invalid_day():
    assert info.clean_days("Mon Wed Aug") == []

def test_clean_days_empty():
    assert info.clean_days("") == []


### clean_time() tests !!!

def test_clean_time_am_am():
    assert info.clean_time("8:00 a.m. - 10:00 a.m.") \
        == {"start":"080000", "end":"100000"}

def test_clean_time_am_pm():
    assert info.clean_time("11:00 a.m. - 1:00 p.m.") \
        == {"start":"110000", "end":"130000"}

def test_clean_time_pm_pm():
    assert info.clean_time("2:00 p.m. - 3:00 p.m.") \
        == {"start":"140000", "end":"150000"}

def test_clean_time_pm_am(): #!!! set the end day to next day
    assert info.clean_time("8:00 p.m. - 6:00 a.m.") \
        == {"start":"200000", "end":"060000"}

def test_clean_time_invalid_time():
    assert info.clean_time("13:00 p.m. - 3:00 a.m.") \
        == {"start":"", "end":"030000"}

def test_clean_time_invalid_time2():
    assert info.clean_time("6:00 a.m. - 26:00 p.m.") \
        == {"start":"060000", "end":""}
    
def test_clean_time_12pm_12am(): #!!! set the end day to next day
    assert info.clean_time("12:00 p.m. - 12:00 a.m.") \
        == {"start":"120000", "end":"240000"}
    

### clean_room() tests

def test_clean_room():
    assert info.clean_room("WESB-Floor 1-Room 100") == "WESB Floor 1 Room 100"