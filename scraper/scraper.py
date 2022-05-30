from pathlib import Path

from .lib.config import ConfigFile
from .lib.jobscraper import JobsCZScraper

# from .lib.debugging import debugging


def scrapers() -> dict:

    _BASE_DIR = Path(__file__).resolve().parent
    _cfg = ConfigFile(_BASE_DIR, debug=False)

    scrapers_objects = [
        JobsCZScraper(_cfg, "jobs.cz"),
    ]

    for scrap in scrapers_objects:
        for obj in scrap.prepare_data():
            yield obj
