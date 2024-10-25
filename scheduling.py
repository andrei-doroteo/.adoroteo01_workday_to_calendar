# Andrei Doroteo
# 2024/09/29
#
# This module handles the creation of calendar files (.ics)

from datetime import datetime, timedelta

from icalendar import Calendar, Event, Timezone, TimezoneDaylight, TimezoneStandard


def create_ical(class_schedule: dict, filename: str) -> None:
    """
    ## Inputs
    - class_schedule
        - A dict of a UBC converted ubc schedule

    creates a calendar and adds all classes from class_schedule.
    then downloads the calendar in .ics format.
    """

    calendar = Calendar()

    # Add the timezone component to the calendar
    timezone = create_timezone()

    # Define standard time (winter)
    add_standard_time(timezone)

    # Define daylight time (summer)
    add_daylight_time(timezone)

    # Add the timezone component to the calendar
    calendar.add_component(timezone)

    add_classes(class_schedule, calendar)

    # Write to file
    generate_file(filename, calendar)


def generate_file(filename, calendar):
    with open(filename, "wb") as f:
        f.write(calendar.to_ical())


def add_classes(class_schedule, calendar):
    for class_info in class_schedule:
        event = Event()

        # 20241001T090000
        event.add(
            "dtstart",
            datetime.strptime(
                class_info["Meeting Patterns"]["start_date"]
                + "T"
                + class_info["Meeting Patterns"]["start_time"],
                "%Y%m%dT%H%M%S",
            ),
        )  # Start time
        event.add(
            "dtend",
            datetime.strptime(
                class_info["Meeting Patterns"]["start_date"]
                + "T"
                + class_info["Meeting Patterns"]["end_time"],
                "%Y%m%dT%H%M%S",
            ),
        )  # End time

        rrule = {
            "freq": "weekly",  # Frequency: weekly
            "wkst": "SU",  # Week start on Sunday
            "byday": class_info["Meeting Patterns"]["days"],  # Repeat on
            "until": datetime.strptime(
                class_info["Meeting Patterns"]["end_date"] + "T" + "235959",
                "%Y%m%dT%H%M%S",
            ),
        }
        event.add("rrule", rrule)

        event.add(
            "location", class_info["Meeting Patterns"]["room"]
        )  # Optional location

        event.add("summary", class_info["Section"])  # Class name/title

        calendar.add_component(event)


def add_daylight_time(timezone: Timezone) -> None:
    """
    ## Input
    - timezone
        - an icalendar TimeZone object

    sets the daylight timezone of timezone to Vancouver
    daylight savings time
    """

    tz_daylight = TimezoneDaylight()
    tz_daylight.add("tzname", "PDT")
    tz_daylight.add("dtstart", datetime(2024, 3, 10, 2, 0, 0))
    tz_daylight.add("tzoffsetfrom", timedelta(hours=-8))
    tz_daylight.add("tzoffsetto", timedelta(hours=-7))
    timezone.add_component(tz_daylight)


def add_standard_time(timezone: Timezone) -> None:
    """
    ## Input
    - timezone
        - an icalendar TimeZone object

    sets the standard timezone of timezone to Vancouver
    standard time
    """

    tz_standard = TimezoneStandard()
    tz_standard.add("tzname", "PST")
    tz_standard.add("dtstart", datetime(2024, 11, 1, 2, 0, 0))
    tz_standard.add("tzoffsetfrom", timedelta(hours=-7))
    tz_standard.add("tzoffsetto", timedelta(hours=-8))
    timezone.add_component(tz_standard)


def create_timezone() -> Timezone:
    """
    ## Returns
    - a timezone object with time zone id of 'America/Vancouver'
    """

    timezone = Timezone()
    timezone.add("tzid", "America/Vancouver")
    return timezone


# # Example class schedule
# class_schedule = [

#     {
#         "Section": "STAT 200 103",
#         "Meeting Patterns":
#             {
#                 "start_date": "20240903",
#                 "end_date": "20241206",
#                 "days": ["MO", "WE", "FR"],
#                 "start_time": "140000",
#                 "end_time": "150000",
#                 "room": "WESB Floor 1 Room 100",
#             }
#         ,
#     }
#     # {
#     #     'class_name': 'Pharmacy 101',
#     #     'start_time': datetime(2024, 10, 1, 9, 0, 0),  # Start time: Oct 1, 2024, 9:00 AM
#     #     'end_time': datetime(2024, 10, 1, 10, 0, 0),   # End time: Oct 1, 2024, 10:00 AM
#     #     'location': 'Room 204',
#     #     'recurrence': True,  # Weekly class
#     #     'recurrence_end': datetime(2024, 12, 15, 0, 0, 0)  # Ends on Dec 15, 2024
#     #  }#,
#     # {
#     #     'class_name': 'Portuguese 101',
#     #     'start_time': datetime(2024, 10, 3, 11, 0, 0),
#     #     'end_time': datetime(2024, 10, 3, 12, 30, 0),
#     #     'location': 'Room 310',
#     #     'recurrence': True,
#     #     'recurrence_end': datetime(2024, 12, 20, 0, 0, 0)
#     # }
# ]

# # Generate the iCal file
# create_ical(class_schedule, "my_class_schedule.ics")
