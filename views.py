import argparse
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--path", type=Path,
        default="tables/wine3.xlsx"
        )

    return parser


def get_wines(products):
    wines = defaultdict(list)
    for product in products:
        wines[product["Категория"]].append(product)
    wines = sorted(wines.items())
    return wines


def years(first_year):
    current_year = datetime.now().year
    delta = current_year - first_year
    listofyears = ['лет', 'год', 'года']
    num = delta % 100
    if num >= 11 and num <= 19:
        year = listofyears[1]
    else:
        i = delta % 10
        if i == 1:
            year = listofyears[1]
        elif i in [2, 3, 4]:
            year = listofyears[2]
        else:
            year = listofyears[0]
    return f'{delta} {year}'
