"""constants."""

__version__ = "0.0.0"

BASE_URL = "https://secure.pupilasset.com/api/parentAppv4.php?appVersion=5&action={ACTION}"
CALENDAR_URL = "https://secure.pupilasset.com/api/timeCal.php?appVersion=5&action={ACTION}"

USER_AGENT = "okhttp/3.4.1"

LOGIN_SUCCESS_MESSAGE = "Logged in OK"
LOGIN_FAILED_MESSAGE = "Please check your log in details"

# Define a dictionary to map month abbreviations to month numbers
MONTH_MAPPING = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

# Use regular expressions to extract date components
COOKIE_EXP_REGEX = r"(\w+), (\d+)-(\w+)-(\d+) (\d+:\d+:\d+) .*"

ENDPOINTS = {
    "login": {
        "method": "GET",
        "query_parameters": {
            "username": "",
            "password": ""
        }
    },
    "getCoreInfo": {
        "method": "GET"
    },
    "getPupilsOfParent": {
        "method": "GET"
    },
    "getTimeCal": {
        "url": CALENDAR_URL,
        "method": "GET",
        "query_parameters": {
            "whatJSON": "",
            "theDate": "",
            "switch": "PARENTS",
            "pupilRef": ""
        }
    }
}
