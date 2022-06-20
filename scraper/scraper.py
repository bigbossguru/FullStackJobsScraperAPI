from pathlib import Path
import logging

from .lib.config import ConfigFile
from .lib.jobscraper import JobsCZScraper

# from .lib.debugging import debugging


def scrapers() -> dict:

    logging.basicConfig(format='[%(asctime)s][%(name)6s][%(levelname)7s] %(message)s')
    logger = logging.getLogger('scraper')
    logging.getLogger().setLevel(logging.INFO)

    _BASE_DIR = Path(__file__).resolve().parent
    _cfg = ConfigFile(_BASE_DIR, debug=False)

    scrapers_objects = [
        JobsCZScraper(_cfg, "jobs.cz", logger),
    ]

    for scrap in scrapers_objects:
        for obj in scrap.prepare_data():
            yield obj
