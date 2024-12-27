# Andrei Doroteo
# 2024/09/29
#
# This module handles the creation of calendar files (.ics)

from datetime import datetime, timedelta

from icalendar import (Calendar, Event, Timezone, TimezoneDaylight,
                       TimezoneStandard)


def create_ical(class_schedule: dict) -> Calendar:
    """
    ## Inputs
    - class_schedule
        - A dict of a UBC converted ubc schedule

    creates a calendar and adds all classes from class_schedule
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

    return calendar

    # Write to file
    # generate_file(filename, calendar)


# def generate_file(filename, calendar):
#     with open(filename, "wb") as f:
#         f.write(calendar.to_ical())


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
