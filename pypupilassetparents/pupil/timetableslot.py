"""Defines a single slot of a timetable."""

from datetime import time

def parse_time(raw: str) -> time:
    """Converts a string to a time."""
    split = raw.split(":")
    return time(hour=int(split[0]), minute=int(split[1]))

class TimetableSlot:
    """A instance of a timetable slot."""

    def __init__(self) -> None:
        """Use the from_dict method to init this class."""
        self.slot_id: int = None
        self.title: str = None
        self.day_of_week: int = None
        self.start_time: time = None
        self.end_time: time = None

    @classmethod
    def from_dict(cls, raw: dict) -> 'TimetableSlot':
        """Converts a raw response to a object."""
        self = cls()
        self.slot_id = raw["slotID"]
        self.title = raw["title"]
        self.day_of_week = raw["dayOfWeek"]
        self.start_time = parse_time(raw["startTime"])
        self.end_time = parse_time(raw["endTime"])
        return self
