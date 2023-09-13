"""Test module."""


import logging
import asyncio
from pypupilassetparents import PupilAsset

_LOGGER = logging.getLogger(__name__)

async def main():
    """Main func"""
    login = True
    while login:
        try:
            use_cookies = input("Use cookies? [N/y]").upper()
            if use_cookies == "Y":
                control = await PupilAsset.login(
                    None, None, {
                        "ai_operationid": input("Enter ai_operationid cookie: "),
                        "asset": input("Enter asset cookie: ") 
                    }
                )
            else:
                control = await PupilAsset.login(
                    username=input("Username: "),
                    password=input("Password: ")
                )
            login = False
        except Exception as err:
            _LOGGER.error(err)

    while True:
        for p in control.pupils:
            _LOGGER.debug("Discovered pupil %s", p.pupil_id)
            for period in p.timetable.build_today_timetable_calendar:
                _LOGGER.debug("Found period %s starting at %s on date %s",
                              period.title,
                              period.start_time,
                              period.class_date)
        for term in control.school.terms:
            _LOGGER.debug("Discovered new term %s", term.term_date_id)
        _LOGGER.debug("Ping")
        await asyncio.sleep(60)
        _LOGGER.debug("Pong")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
