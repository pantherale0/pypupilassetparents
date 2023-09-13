"""Pupil Asset Exceptions"""

class HttpException(Exception):
    """A HTTP Exception occured."""

    def __init__(self, status, response) -> None:
        super().__init__("HTTP Exception Occured", status)
        self.response = response

class InvalidCredentials(Exception):
    """Invalid credentials provided."""

    def __init__(self) -> None:
        super().__init__("The provided username or password was incorrect.")
