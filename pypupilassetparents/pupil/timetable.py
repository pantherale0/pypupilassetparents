"""Defines a timetable."""

from datetime import time, datetime, timedelta, date
from .timetableslot import (
    TimetableSlot,
    parse_time
)

class Timetable:
    """A instance of a timetable"""
    def __init__(self) -> None:
        """Init a timetable.
        Use from_dict to correctly init this object"""
        self.week_span: int = None
        self.day_span: int = None
        self.start_of_week: int = None
        self.total_daily_slots: int = None
        self.lunch_start: time = None
        self.lunch_end: time = None
        self.academic_year: int = None
        self.timetable_raw: dict = {}
        self.slots: list[TimetableSlot] = []

    @property
    def build_today_timetable_calendar(self) -> list['TimetableEntry']:
        """Returns a dict containing all of the timetable."""
        built = []
        today = datetime.now()
        for slot in self.slots:
            day = today.weekday() - slot.day_of_week
            day = today-timedelta(days=day)
            if slot.end_time > self.lunch_start:
                built.append(TimetableEntry(
                    title="Lunch",
                    start_time=self.lunch_start,
                    end_time=self.lunch_end,
                    class_date=day.date()
                ))
            built.append(TimetableEntry(
                title="CLASS",
                start_time=slot.start_time,
                end_time=slot.end_time,
                class_date=day.date(),
                class_name="Unknown",
                teacher="Unknown"
            ))
        return built

    @classmethod
    def from_dict(cls, raw: dict) -> 'Timetable':
        """Converts a raw response to a timetable."""
        self = cls()
        self.week_span = raw["timetable"]["weekSpan"]
        self.day_span = raw["timetable"]["daySpan"]
        self.start_of_week = raw["timetable"]["startOfWeek"]
        self.total_daily_slots = raw["timetable"]["numSlots"]
        self.lunch_start = parse_time(raw["timetable"]["lunchStartTime"])
        self.lunch_end = parse_time(raw["timetable"]["lunchEndTime"])
        self.academic_year = raw["timetable"]["academicYear"]
        self.timetable_raw = None
        for slot_id in raw["timetable"]["slots"]:
            self.slots.append(TimetableSlot.from_dict(
                raw["timetable"]["slots"][slot_id]
            ))
        return self


class TimetableEntry:
    """Defines a entry on a timetable."""

    def __init__(self,
                 title: str,
                 class_date: date,
                 start_time: time,
                 end_time: time,
                 teacher: str = None,
                 class_name: str = None) -> None:
        """Init a entry."""
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.teacher = teacher
        self.class_name = class_name
        self.class_date = class_date
