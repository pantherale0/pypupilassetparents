"""The core API handler."""

import logging
import json
import re
from datetime import datetime
from urllib.parse import quote

import aiohttp
import aiohttp.client_exceptions

from .const import (
    ENDPOINTS,
    BASE_URL,
    LOGIN_SUCCESS_MESSAGE,
    LOGIN_FAILED_MESSAGE,
    USER_AGENT,
    MONTH_MAPPING,
    COOKIE_EXP_REGEX
)
from .exceptions import HttpException, InvalidCredentials

_LOGGER = logging.getLogger(__name__)

class PupilAssetAPI:
    """Core web API handler."""

    def __init__(self, cookies: dict = None):
        """Initialize attrs for the core API."""
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(cookies=cookies)
        self._session.headers.add("user-agent", USER_AGENT)
        self._reauth_at: datetime = None
        self._username: str = None
        self._password: str = None

    async def login(self, username: str = None, password: str = None):
        """Handle a login request."""
        if username is None or password is None:
            username = self._username
            password = self._password
        self._username = username
        self._password = password
        response = await self.request_handler("login", username=username, password=password)
        if response["status"] == 200 and response["json"]["msg"] == LOGIN_SUCCESS_MESSAGE:
            return True
        if response["status"] == 200 and response["json"]["msg"] == LOGIN_FAILED_MESSAGE:
            raise InvalidCredentials()
        raise RuntimeError("Unknown login state, please report this as an issue.")

    @classmethod
    async def create(cls, username: str, password: str, cookies: dict = None) -> 'PupilAssetAPI':
        """Login to the API using the provided username and password."""
        api = cls(cookies)
        if cookies is None:
            await api.login(username, password)
        return api

    async def close(self):
        """Ends the aiohttp session."""
        await self._session.close()

    async def request_handler(self, endpoint: str, body: dict = None, **kwargs):
        """Handle an API request."""
        # handle reauthentication.
        if endpoint != "login" and self._reauth_at<=datetime.now():
            await self.login()

        _LOGGER.debug("Got request for %s", endpoint)
        # first get the request config from the endpoint map.
        epoint = ENDPOINTS.get(endpoint, None)
        if epoint is None:
            raise ValueError("Endpoint not defined.")

        query_parameters = epoint.get("query_parameters", {})
        url: str = epoint.get("url", BASE_URL)
        url = url.format(
            ACTION=endpoint
        )

        for arg in query_parameters:
            _LOGGER.debug("Processing argument %s", arg)
            url = url + f"&{arg}={quote(kwargs.get(arg))}"

        async with self._session.request(
            method=epoint.get("method", "GET"),
            url=url,
            json=body
        ) as request:
            try:
                response = {
                    "status": request.status,
                    "json": await request.json(),
                    "text": await request.text()
                }
            except aiohttp.client_exceptions.ContentTypeError:
                try:
                    response = {
                    "status": request.status,
                    "json": json.loads(await request.text()),
                    "text": await request.text()
                }
                except json.JSONDecodeError:
                    _LOGGER.warning("No JSON available due to content error.")
                    response = {
                        "status": request.status,
                        "json": {},
                        "text": await request.text()
                    }
            _LOGGER.debug("Response for request %s is %s", endpoint, request.status)
            if not (request.status >= 200 and request.status < 300):
                raise HttpException(request.status, response)
            if endpoint == "login":
                # set reauth interval
                match = re.match(COOKIE_EXP_REGEX, request.cookies.get("asset").get("expires"))
                if match:
                    day_of_week, day, month_abbrev, year, time = match.groups()
                    _LOGGER.debug("Got day of week %s", day_of_week)
                    # Convert month abbreviation to month number
                    month = MONTH_MAPPING[month_abbrev]
                    self._reauth_at = datetime(
                        int(year),
                        month,
                        int(day),
                        *map(int, time.split(":")))

            return response
