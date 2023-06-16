from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from config.urls import PORSCHE_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():
    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'parasoft_dependencies'
    table_name = 'all_dependencies'
    company_name = 'porsche'
    db.create_table(table_name)

    html_text = requests.get(PORSCHE_URL).text

    pattern = r'(?<=\*{5}\n)(.*?)(?=\n\*{5})'

    dependencies = re.findall(pattern, html_text)

    package_name_set = set()

    for index, element in enumerate(dependencies):
        if element.lower() not in package_name_set:
            value = remove_at_symbol(element)
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
