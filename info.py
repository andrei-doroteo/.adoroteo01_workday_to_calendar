### Andrei Doroteo
### 2024/08/17


def get_name(section:str, name:str="") -> str:
    """
    consumes a section provided by workday. produces the class name in the format "<class name> <class number> <section>".
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


def handle_meeting_patterns(mp:str, days:str="", time:str="", room:str="", counter:int=0) -> dict:
    """
    consumes meeting pattern on workday schedule. produces a dict of days, time, and room of the course
    """
    # 2024-09-03 - 2024-12-06 | Mon Wed Fri | 2:00 p.m. - 3:00 p.m. | WESB-Floor 1-Room 100 !!!
    if mp == "":
       return {"days":convert_days(days), "time":convert_time(time), "room":convert_room(room)}
    
    else:
       if mp[0] == " " and mp[1] == "|" and mp[2] == " ":
            return handle_meeting_patterns(mp=mp[3:], days=days, time=time, room=room, counter = counter + 1)
       
       else:
            if counter == 0:
                return handle_meeting_patterns(mp=mp[1:], counter=counter)
            
            elif counter == 1:
                return handle_meeting_patterns(mp=mp[1:], days = days + mp[0], counter=counter)
            
            elif counter == 2:
                return handle_meeting_patterns(mp=mp[1:], days=days, time = time + mp[0], counter=counter)
            
            elif counter == 3:
                return handle_meeting_patterns(mp=mp[1:], days=days, time=time, room = room + mp[0], counter=counter)
   
