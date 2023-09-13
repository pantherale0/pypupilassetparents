"""Core Pupil Asset entry point."""

from .api import PupilAssetAPI
from .school import School
from .pupil import Pupil

class PupilAsset:
    """Core Pupil Asset functions"""

    def __init__(self, api: PupilAssetAPI) -> None:
        """Initialize Pupil Asset."""
        self.school: School = None
        self.pupils: list[Pupil] = []
        self.pupil_school: dict = {}
        self._api: PupilAssetAPI = api
        self._core_data: dict = None

    async def update(self):
        """Update instance data."""
        await self._fetch_core_data()
        await self._fetch_pupil_data()

    async def _fetch_core_data(self):
        """Internal fetch core data."""
        response = await self._api.request_handler("getCoreInfo")
        response = response["json"]
        if self.school is None:
            self.school = School.from_dict(response["school"], self._api)
        self.school.update(response)

    async def _fetch_pupil_data(self):
        """Internal fetch basic pupil data."""
        response = await self._api.request_handler("getPupilsOfParent")
        response = response["json"]
        for pupil_raw in response.get("pupils", []):
            try:
                self.get_pupil(pupil_raw["pupilID"]).update(pupil_raw)
                await self.get_pupil(pupil_raw["pupilID"]).get_timetable()
            except ValueError:
                pupil = Pupil.from_dict(pupil_raw, self._api)
                await pupil.get_timetable()
                self.pupils.append(pupil)
                self.pupil_school[pupil.pupil_id] = pupil_raw["schoolID"]

    def get_pupil(self, pid) -> Pupil:
        """Returns a single pupil."""
        discovered = [x for x in self.pupils if x.pupil_id == pid]
        if len(discovered) > 0:
            return discovered[0]
        raise ValueError("Pupil ID not yet discovered.")

    @classmethod
    async def login(cls, username: str, password: str, cookies: dict = None):
        """Login and create an instance of Pupil Asset."""
        auth = await PupilAssetAPI.create(username, password, cookies)
        self = cls(auth)
        await self.update()
        return self
