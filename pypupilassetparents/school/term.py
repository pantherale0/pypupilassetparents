"""A definition of a school term."""

from datetime import datetime, date

class Term:
    """A school term."""
    def __init__(self,
                 term_date_id,
                 timetable_id,
                 academic_year,
                 term,
                 mid_term,
                 start_date,
                 end_date,
                 current,
                 starting_wk):
        """Init a school term"""
        self.term_date_id: int = int(term_date_id)
        self.timetable_id: int = int(timetable_id)
        self.academic_year: int = int(academic_year)
        self.term: str = str(term)
        self.mid_term: str = str(mid_term)
        self.start_date: date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date: date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.current: int = int(current)
        self.starting_wk: int = int(starting_wk)


    @classmethod
    def from_dict(cls, raw: dict) -> 'Term':
        """Converts a raw response to a term."""
        return cls(
            raw["termDateID"],
            raw["timetableID"],
            raw["academicYear"],
            raw["term"],
            raw["midTerm"],
            raw["startDate"],
            raw["endDate"],
            raw["current"],
            raw["startingWk"]
        )
