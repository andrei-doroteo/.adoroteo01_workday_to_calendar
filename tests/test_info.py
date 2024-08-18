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

### 