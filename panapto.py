from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import PANAPTO_URL
import re
from utils.database import Database
from utils.selenium import get_dynamic_html
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'panapto_dependencies'
    table_name = 'all_dependencies'
    company_name = 'panapto'
    db.create_table(table_name)

    html_text = get_dynamic_html(PANAPTO_URL)

    soup = BeautifulSoup(html_text, 'lxml')

    elements = soup.select('body table > tbody > tr > td:nth-child(1)')

    package_name_set = set()
    for element in elements[1:]:
        if element.text.lower() not in package_name_set:
            value = remove_at_symbol(element.text.strip())
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
