from pathlib import Path
import json


class ConfigFile:
    def __init__(self, filepath: str) -> None:
        self.filepath = Path(filepath)
        self._check_exist_config_file()
        self._read()

    def _read(self) -> None:
        with open(self.filepath, encoding="utf-8", mode="r") as file:
            self.config = json.load(file)

    def _check_exist_config_file(self) -> None | Exception:
        if not self.filepath.exists():
            raise FileNotFoundError(f"Missing config file: {self.filepath}")
