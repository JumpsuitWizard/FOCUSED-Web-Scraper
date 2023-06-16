from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import CONFLUENT_URL
import re
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'confluent_dependencies'
    table_name = 'all_dependencies'
    company_name = 'confluent'
    db.create_table(table_name)

    html_text = requests.get(CONFLUENT_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#t01 > tbody > tr > td:nth-child(1)')
    package_name_set = set()
    for package_name in elements[1:]:
        if package_name.text.lower() not in package_name_set:
            package_name_set.add(package_name.text.lower())
            package = remove_at_symbol(package_name.text)
            db.insert_dependency(package, table_name, company_name)


scrape_dependencies()
