### Andrei Doroteo
### 2024/08/17



def get_name(section:str, name:str="") -> str:
    """
    consumes a section provided by workday. 
    produces the class name in the format: 
    "<class name> <class number> <section>".


    returns "" if the section is invalid
    """

    try:
        if section == "":
           return section
        
        elif section[0] == " " and section[1] == "-" and section[2] == " ":
         return name.replace('_V', '').replace('-', ' ')
    
        else:
            return get_name(section=section[1:], name = name + section[0])
    
    except IndexError:
        print("Invalid Section") # !!! Handle error better in final app
        return ""



def handle_meeting_patterns(mp:str, dates:str="", days:str="",
                             time:str="", room:str="",
                               counter:int=0) -> dict:
    """
    consumes meeting pattern on workday schedule. 
    produces a dict of days, time, and room of the course

    CONSTRAINTS: mp must be in the format: 
                 <section 1> | <day 1> <day 2> <...> |
                 <time> <period> - <time> <period> | <room>-<floor>-<#>
    """
    # Starting Value: "2024-09-03 - 2024-12-06 | Mon Wed Fri | 2:00 p.m. - 3:00 p.m. | WESB-Floor 1-Room 100" !!! delete

    if mp == "": # base case
       times = clean_time(time)
       dates = clean_dates(dates)

       return {"start_date":dates["start"],
               "end_date":dates["end"],
               "days":clean_days(days),
               "start_time": times["start"],
               "end_time": times["end"],
               "room":clean_room(room)}
    
    else:
       if mp[0] == " " and mp[1] == "|" \
        and mp[2] == " ": # increase counter at seperator
            return handle_meeting_patterns(mp=mp[3:], dates=dates, days=days,
                                            time=time, room=room,
                                            counter = counter + 1)
       
       else:
            if counter == 0: # add 1st section to dates.
                return handle_meeting_patterns(mp=mp[1:],
                                                dates = dates + mp[0],
                                                counter=counter)
            
            elif counter == 1: # add 2nd section to days
                return handle_meeting_patterns(mp=mp[1:], dates=dates,
                                                days = days + mp[0],
                                                counter=counter)
            
            elif counter == 2: # add 3rd section to time
                return handle_meeting_patterns(mp=mp[1:], dates=dates,
                                                days=days,
                                                time = time + mp[0],
                                                counter=counter)
            
            elif counter == 3: # add 4th section to room
                return handle_meeting_patterns(mp=mp[1:], dates=dates,
                                                days=days,
                                                time=time, room = room + mp[0],
                                                counter=counter)



def clean_dates(dates:str) -> dict:
    """
    convert date span from workday meeting patterns into a dictionary
    with a start and end date in the format YYYYMMMDD

    """

    def reformat(date:str) -> str:
        return date.replace("-","")

    # starting value: "2024-09-03 - 2024-12-06"

    dates_split = dates.split(" - ")
    converted_dates = list(map(reformat, dates_split))

    return {"start":converted_dates[0], "end":converted_dates[1]}


def clean_days(days:str) -> list:
    """
    convert course days from workday meeting patterns (ex/ "Tue Thu")
    into a list in the format [SU, MO, TU, WE, TH, FR, SA]

    returns [] if there is an invalid day
    """

    def convert_days(lod:list) -> list:

        conversions = {"Sun":"SU", "Mon":"MO", "Tue":"TU",
                    "Wed":"WE", "Thu":"TH", "Fri":"FR", "Sat":"SA"}
        
        days_list = []

        try:
            for day in lod:
                days_list.append(conversions[day])

            return days_list
        
        except KeyError:
            print("Invalid Day") # !!! handle this in final app

            return []

    days_split = days.split(" ")

    return convert_days(days_split)



def clean_time(time:str) -> dict:
    """
    convert course times from worday meeting patterns 
    (ex/ "2:00 p.m. - 3:00 p.m.")
    into a dict in the format {"start": "HHMMSS", "end": "HHMMSS"}
    """

    def is_pm(time:str) -> bool:
        """
        returns true if string contains "p.m."
        """
        return "p.m." in time
    
    def is_am(time:str) -> bool:
        """
        returns true if string contains "a.m."
        """
        return "a.m." in time

    def convert_format(time:str) -> str:
        """
        converts a time in the format: "HH:MM a.m." or "H:MM a.m."
                                       "HH:MM p.m."    "H:MM p.m."
        into 24hr format HHMMSS
        """

        if is_pm(time):
            removed_suffix = time.removesuffix(" p.m.")
            hours_minutes = removed_suffix.split(":")
            hours_minutes[0] = int(hours_minutes[0])
            if hours_minutes[0] > 12:
                print("time out of range") # !!! handle better
                return "" 
            
            elif hours_minutes[0] == 12: # 12pm = 120000
                hours_minutes[0] = str(hours_minutes[0])

            else:
                hours_minutes[0] += 12
                hours_minutes[0] = str(hours_minutes[0])

            return hours_minutes[0] + hours_minutes[1] + "00"

        elif is_am(time):
            removed_suffix = time.removesuffix(" a.m.")
            hours_minutes = removed_suffix.split(":")

            hours_minutes[0] = int(hours_minutes[0])

            if hours_minutes[0] > 12:
                print("time out of range") # !!! handle properly later
                return ""
            
            elif hours_minutes[0] == 12: # 12am = 240000
                hours_minutes[0] += 12
                hours_minutes[0] = str(hours_minutes[0])
            
            elif hours_minutes[0] < 10:
                hours_minutes[0] = "0" + str(hours_minutes[0])

            else:
                hours_minutes[0] = str(hours_minutes[0])

            return hours_minutes[0] + hours_minutes[1] + "00"

        else:
            print("time has invalid format") # !!! handle properly in final app
            return ""

    time_split = time.split(" - ")

    time_converted = list(map(convert_format, time_split))

    return {"start":time_converted[0], "end":time_converted[1]}



def clean_room(room:str) -> str:
    """
    convert room name from worday meeting patterns
    into a string with proper spaces and without "-"
    """
    
    return room.replace("-", " ")



def convert_date(date:str) -> str:
    """
    converts start or end date from workday (ex/ 2024-09-03)
    and produces the date in YYYYMMDD format

    CONSTRAINT: date must be in YYYY-MM-DD format
    """

    return date.replace("-", "")