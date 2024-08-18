import sys
sys.path.append("./")
import info

### get_name() tests

def test_get_name():
    assert info.get_name(section="STAT_V 200-103 - Elementary Statistics for Applications") == "STAT 200 103"

def test_get_name_empty_string():
    assert info.get_name(section="") == ""

def test_get_name_break_begining():
    assert info.get_name(section=" -CPSC 200") == ""

def test_get_name_no_break():
    assert info.get_name(section="CPSC 200 201") == ""

### handle_meeting_patterns() tests

def test_handle_meeting_patterns():
    assert info.handle_meeting_patterns(mp="2024-09-03 - 2024-12-06 | Mon Wed Fri | 2:00 p.m. - 3:00 p.m. | WESB-Floor 1-Room 100") \
    == {"days":"Mon Wed Fri", "time":"2:00 p.m. - 3:00 p.m.", "room":"WESB-Floor 1-Room 100"}