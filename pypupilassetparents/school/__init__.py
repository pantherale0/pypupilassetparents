"""The school module for Pupil Asset."""

from datetime import date, datetime

from pypupilassetparents.api import PupilAssetAPI
from .term import Term

class School:
    """Defines a school."""

    def __init__(self, api: PupilAssetAPI) -> None:
        self._api = api
        self.school_id = None
        self.school_name = None
        self.school_type = None
        self.status = None
        self.lea = None
        self.estab = None
        self.start_year_group = None
        self.end_year_group = None
        self.picture = None
        self.address = None
        self.postcode = None
        self.latitude = None
        self.longitude = None
        self.website = None
        self.phone_number = None
        self.terms: list[Term] = None
        self.other_holidays: list[date] = None

    def _parse_my_terms(self, raw: list[dict]):
        """Parses terms for this school from getCoreInfo response."""
        parsed = []
        for term in raw:
            parsed.append(Term.from_dict(term))
        self.terms = parsed

    def get_current_term(self) -> Term:
        """Gets the current term."""
        terms = [x for x in self.terms
             if x.start_date >= date.today() and x.end_date <= date.today()]
        if len(terms)>0:
            return terms[0]
        raise ValueError("No active term.")

    def _parse_other_holidays(self, raw: dict):
        """Converts the otherHolidaysArray value and parses into self.other_holidays"""
        self.other_holidays = [
            datetime.strptime(
                item[str(i)]["calendarDate"], "%Y-%m-%d"
            ).date()
            for i, item in enumerate(raw) if str(i) in item]

    def update(self, core_response: dict):
        """Updates data using a provided core info request response"""
        self._parse_other_holidays(core_response.get("otherHolidaysArray", []))
        self._parse_my_terms(core_response.get("termDates", []))

    @classmethod
    def from_dict(cls, raw: dict, api: PupilAssetAPI) -> 'School':
        """Parses a raw dict"""
        self = cls(api)
        self.school_id = raw["schoolID"]
        self.school_name = raw["schoolName"]
        self.school_type = raw["schoolType"]
        self.status = raw["status"]
        self.lea = raw["lea"]
        self.estab = raw["estab"]
        self.start_year_group = raw["startYearGroup"]
        self.end_year_group = raw["endYearGroup"]
        self.picture = raw["picture"]
        self.address = raw["address"]
        self.postcode = raw["postcode"]
        self.latitude = raw["lat"]
        self.longitude = raw["lng"]
        self.website = raw["webSite"]
        self.phone_number = raw["schoolPhone"]
        return self
