class Course:

    # a course is course(start, end, byday, name, location)
    # start & end is yyymmddThhmmss (<year><month><day>T<hour><minute><second>)
    # byday is List (MO,TU,WE,TH,FR)
    # name is String
    # location is String

    def __init__(self, start=None, end=None, byday=None, name=None, location=None) -> None:
        self.name=name
        self.start=start
        self.end=end
        self.byday=byday
        self.name=name
        self.location=location

#:VEVENT
# DTSTART;TZID=America/Regina:20240902T080000
# DTEND;TZID=America/Regina:20240902T093000
# RRULE:FREQ=WEEKLY;WKST=SU;BYDAY=MO,WE
# DTSTAMP:20240817T022143Z
# UID:68gdkkq754blojuq0llbvjsjaa@google.com
# CREATED:20240708T032757Z
# LAST-MODIFIED:20240817T022106Z
# LOCATION:TESTROOM 201
# SEQUENCE:1
# STATUS:CONFIRMED
# SUMMARY:STAT201-203
# TRANSP:OPAQUE
# END:VEVENT