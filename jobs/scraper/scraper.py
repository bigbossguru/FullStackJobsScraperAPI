import requests
from bs4 import BeautifulSoup

# from django.db.utils import IntegrityError
# from jobs.models import Job

from lib.config import ConfigFile


def web_scraper() -> None:
    pass


# def web_scraper():
#     metadata = {
#         "title": "search-list__main-info__title__link",
#         "company": "search-list__secondary-info--label notranslate",
#         "address": "search-list__secondary-info--label",
#         "salary": "search-list__tags__label search-list__tags__salary--label",
#     }

#     urls = [
#         "https://www.jobs.cz/prace/?q%5B%5D=python",
#         "https://www.jobs.cz/prace/?q%5B0%5D=python&page=2",
#         "https://www.jobs.cz/prace/?q%5B0%5D=python&page=3",
#     ]

#     for url in urls:
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, "lxml")
#         list_data = soup.find_all("div", class_="standalone search-list__item")

#         prepare_data(list_data, metadata)


# def prepare_data(list_data: list, metadata: dict) -> None:
#     for data in list_data:
#         title = data.find("a", class_=metadata.get("title"))
#         salary = data.find("span", class_=metadata.get("salary"))
#         company_address = data.find_all("span", class_=metadata.get("address"))

#         obj = dict.fromkeys(["position", "company", "address", "salary"], None)
#         if title:
#             obj["position"] = title.text.strip()
#         if salary:
#             parts_of_salary = salary.text.split()
#             obj["salary"] = "".join(parts_of_salary).strip("Kč")
#         if company_address:
#             obj["company"] = company_address[0].text.strip()
#             obj["address"] = "".join(company_address[1].text.split()[1:])
#         if obj:
#             try:
#                 Job.objects.create(**obj)
#             except IntegrityError:
#                 continue

# Only for DEBUG mode
def _debugging_entrypoint() -> None:
    pass


if __name__ == "__main__":
    DEBUG = True
    if DEBUG:
        _debugging_entrypoint()
    else:
        cfg = ConfigFile("/home/boss/Desktop/jobsCZ_API/jobs/scraper/config.json")
        print(cfg.config["sites"]["jobs"])
