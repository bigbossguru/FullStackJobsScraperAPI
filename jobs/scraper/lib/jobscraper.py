from .config import ConfigFile


class JobScraper:
    def __init__(self, config: ConfigFile):
        self.config = config
