def get_name(section:str, name:str="") -> str:
    """
    consumes a section provided by workday. produces the class name in the format "<class name> <class number> <section>"
    """

    try:
        if section == "":
           return section
        
        elif section[0] == " " and section[1] == "-" and section[2] == " ":
         return name.replace('_V', '').replace('-', ' ')
    
        else:
            return get_name(section=section[1:], name = name + section[0])
    
    except IndexError:
        print("Invalid Section") # !!!
        return ""

