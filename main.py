import pandas
import icalendar
from icalendar import Calendar, Event
from  classes import *

### make a schedule

schedule = Calendar()

### get info from excel

## clean excel sheet
def get_info(path:str) -> pandas.DataFrame:
    
    # read excel file
    dataframe = pandas.read_excel(path)

    # filter columns
    dataframe_filtered = filter_df(dataframe)

    # parse columns
    dataframe_parsed = parse_df(dataframe_filtered)


def filter_df(df:pandas.DataFrame) -> pandas.DataFrame:
    columns = []
    pass

def parse_df():
    pass

## get course name from excel




### make all courses in schedule

def make_course(x:Course) -> Course:
    pass
#   EXCel -> Course
 # consumes a excel table and produces a Course with all its info

### add all courses to schedule

### download schedule as calendar file

