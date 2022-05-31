from bs4 import BeautifulSoup
from collections import OrderedDict
import requests
import random
import time
import datetime
import json
import csv
import os


encoding = "utf-8"


def get_page(min_discount: int) -> list[OrderedDict]:
    page = 1
    count_page_with_bad_status = 0
    data_product = []
    while True:
        res = requests.get(
            url=f"https://prom.ua/ua/Noutbuki;{page}?price_local__lte=30000&a714=106474&a11306=107865&a11306=107866&a10006=83770"
        )

        actual_product = ["Закінчується", "В наявності"]
        name_status_attrs = {"class": "NCAFH nnmeh Di45I AKX4e iDLYF"}
        soup = BeautifulSoup(res.text, "lxml")

        for teg_price in soup.find_all("span", attrs={"data-qaid": "old_price"}):
            product = teg_price.find_parent("div", attrs={"class": "NCAFH nnmeh b_0HU Di45I AKX4e"}).find_parent()

            old_price = float(teg_price.get("data-qaprice"))
            new_price = float(teg_price.find_previous_sibling().get("data-qaprice"))
            discount = round((1 - new_price / old_price) * 100, 1)
            status = product.find("div", attrs=name_status_attrs).text

            if status in actual_product and discount > min_discount:
                name = product.find("span", attrs={"class": "uvIdx tg78x WZVc3 GI6Pu"}).text.strip()
                photo_link = product.find("img").get("src")
                bad_link: str = product.find("a").get("href").partition("?token")[0]
                link = f'https://prom.{bad_link.lstrip("/")}'
                try:
                    positive_feedback = int(product.find(
                        "span", attrs={"data-qaid": "short_company_rating"}
                    ).get("data-qapositive"))
                except:
                    positive_feedback = "Not feedback"

                data_product.append(
                    OrderedDict(
                        name=name,
                        new_price=new_price,
                        old_price=old_price,
                        discount=discount,
                        status=status,
                        photo_link=photo_link,
                        link=link,
                        positive_feedback=positive_feedback
                    )
                )

        status_products = soup.find_all("div", attrs=name_status_attrs)

        if not any([status.text.strip() in actual_product for status in status_products]):
            count_page_with_bad_status += 1
        else:
            count_page_with_bad_status = 0

        if count_page_with_bad_status > 3 or len(status_products) < 29:
            break

        page += 1
        time.sleep(random.randrange(2, 7))

    data_product.sort(key=lambda x: (x["discount"], x["positive_feedback"]), reverse=True)
    return data_product


def file_write(data: list[OrderedDict], type_file: str, file_name: str = None, dir_name: str = None):
    file_name = file_name or "discount_used_pc"
    dir_name = dir_name or "pc"
    today = datetime.datetime.now()

    name_file = f"{file_name}_{today.strftime('%H_%M')}.{type_file}"
    pc_today_dir = _create_today_directory(dir_name)
    path_file_name = os.path.join(pc_today_dir, name_file)

    with open(path_file_name, "w", encoding=encoding, newline="") as file:
        if type_file == "json":
            json.dump(data, file, indent=4, ensure_ascii=False)
        elif type_file == "csv":
            writer = csv.writer(file)
            writer.writerow(
                ("name", "new_price", "old_price", "discount", "status", "photo_link", "link", "positive_feedback")
            )
            writer.writerows(
                [tuple(product.values()) for product in data]
            )
        else:
            raise ValueError(f"Type_file mast be [json, csv] your type_file [{type_file}]")


def _create_today_directory(name_dir: str) -> str:
    today = datetime.date.today()

    pc_dir = os.path.join(os.getcwd(), name_dir)
    pc_today_dir = os.path.join(pc_dir, today.strftime("%d_%m_%Y"))

    if not os.path.exists(pc_dir):
        os.mkdir(pc_dir)

    if not os.path.exists(pc_today_dir):
        os.mkdir(pc_today_dir)
    return pc_today_dir
