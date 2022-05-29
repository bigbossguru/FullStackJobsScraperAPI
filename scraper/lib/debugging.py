import requests
from bs4 import BeautifulSoup
import pandas as pd

from lib.config import ConfigFile


# Debugging testing file
FILE_NAME = "test_data.csv"


def debugging(config: ConfigFile) -> None:

    # print(config.get_object_by_name_service(service_name="jobss.cz"))
    df_list_data = []
    for site in config.get_sites():

        for url in site["urls"]:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "lxml")
            list_data = soup.find_all(site["tags"]["list"]["tag"], class_=site["tags"]["list"]["class"])

            df = _prepare_data(list_data, site["tags"]["element"])
            df_list_data.append(df)

        break

    result_df = pd.concat(df_list_data)
    result_df.to_csv(config.temp_dir / FILE_NAME)


def _prepare_data(list_data: list, metadata: dict) -> pd.DataFrame:
    objects = []
    for data in list_data:
        obj = dict.fromkeys(["title", "company", "address", "salary"], None)

        title = data.find(metadata["title"]["tag"], class_=metadata["title"]["class"])
        salary = data.find(metadata["salary"]["tag"], class_=metadata["salary"]["class"])
        address = data.find_all(metadata["address"]["tag"], class_=metadata["address"]["class"])
        company = data.find_all(metadata["company"]["tag"], class_=metadata["company"]["class"])

        if title:
            obj["title"] = title.text.strip()
        if salary:
            obj["salary"] = salary.text.strip()
        if company:
            obj["company"] = company[0].text.strip()
        if address:
            address = address[1].text.strip().split("\n")
            obj["address"] = address[-1].strip()
        if obj:
            objects.append(obj)

    return pd.DataFrame(data=objects)
