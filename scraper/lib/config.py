import os
from pathlib import Path
import json
from typing import Callable


def validator_service_name(func: Callable):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return result
        raise ValueError(f"Does not exist this service name {args}, {kwargs.get('service_name')}")

    return inner


class ConfigFile:
    TEMPORARY_FILES_DIR = "lib/temp"
    CONFIG_FILE_NAME = "config.json"

    def __init__(self, base_dir: str | Path, debug: bool = False) -> None:
        self.debug = debug
        self.base_dir = Path(base_dir)
        self.temp_dir: Path = base_dir / ConfigFile.TEMPORARY_FILES_DIR
        self.filepath: Path = base_dir / ConfigFile.CONFIG_FILE_NAME
        self._check_exist_config_file()
        self._prepare_config_settings()

        if debug:
            self._create_temp_folder()

    def _prepare_config_settings(self):
        self.config: dict = self._read()
        self._urls_by_page_count()

    def _read(self) -> None:
        with open(self.filepath, encoding="utf-8", mode="r") as file:
            return json.load(file)

    def _check_exist_config_file(self) -> None | Exception:
        if not self.filepath.exists():
            raise FileNotFoundError(f"Missing config file: {self.filepath}")

    def _urls_by_page_count(self) -> None:
        for site in self.config["sites"]:
            site["urls"] = []
            page_cnt = int(site["page_count"])
            if page_cnt:
                for page in range(1, page_cnt + 1):
                    for lang in self.config["languages"]:
                        site["urls"].append(str(site["url"]).format(language=lang, page=page))

    def _create_temp_folder(self) -> None:
        if not self.temp_dir.exists():
            os.mkdir(self.temp_dir)

    def get_sites(self) -> list[dict]:
        return self.config["sites"]

    @validator_service_name
    def get_service_by_name(self, service_name: str) -> dict | None:
        for site in self.get_sites():
            if service_name.lower() == site["name"].lower():
                return site
        return None

    def get_list_object_tag_classname(self, service_name: str) -> dict:
        site = self.get_service_by_name(service_name)
        return {"name": site["tags"]["list"]["tag"], "class_": site["tags"]["list"]["class"]}

    def get_elem_object_tag_classname(self, service_name: str, element_name: str) -> dict:
        site = self.get_service_by_name(service_name)
        return {
            "name": site["tags"]["element"][element_name]["tag"],
            "class_": site["tags"]["element"][element_name]["class"],
        }
