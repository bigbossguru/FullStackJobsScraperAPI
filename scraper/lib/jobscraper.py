# Standart Python library
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Library for webscraper
import requests
from bs4 import BeautifulSoup, ResultSet

from .config import ConfigFile


@dataclass
class ScraperBase(ABC):
    config: ConfigFile
    service_name: str

    def receive_content_from_service(self) -> ResultSet:
        for url in self.config.get_service_by_name(self.service_name).get("urls"):
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "lxml")
            yield soup.find_all(**self.config.get_list_object_tag_classname(self.service_name))

    @abstractmethod
    def prepare_data(self) -> dict:
        pass


class JobsCZScraper(ScraperBase):
    def prepare_data(self) -> dict:

        for sets_data in self.receive_content_from_service():
            for data in sets_data:
                _object = dict.fromkeys(["position", "company", "address", "salary"], None)

                position = data.find(**self.config.get_elem_object_tag_classname(self.service_name, "position"))
                company = data.find_all(**self.config.get_elem_object_tag_classname(self.service_name, "company"))
                address = data.find_all(**self.config.get_elem_object_tag_classname(self.service_name, "address"))
                salary = data.find(**self.config.get_elem_object_tag_classname(self.service_name, "salary"))

                if position:
                    _object["position"] = position.text.strip()
                if salary:
                    _object["salary"] = salary.text.strip()
                if company:
                    _object["company"] = company[0].text.strip()
                if address:
                    address = address[1].text.strip().split("\n")
                    _object["address"] = address[-1].strip()

                if all([position, company, address]):
                    yield _object


class PraceCZScraper(ScraperBase):
    def prepare_data(self) -> dict:
        for sets_data in self.receive_content_from_service():
            for data in sets_data:
                _object = dict.fromkeys(["position", "company", "address", "salary"], None)
