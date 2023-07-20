from bs4 import BeautifulSoup
import requests
import psycopg2
from utils.database import Database
from config.urls import PARSEC_URL
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'parsec_dependencies'
    table_name = 'all_dependencies'
    company_name = 'parsec'
    db.create_table(table_name)

    html_text = requests.get(PARSEC_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.select(
        'div.c-iTnllM td:nth-child(1) > a')

    package_name_set = set()

    for element in dependencies:
        if element.text.lower() not in package_name_set:
            package_name_set.add(element.text.lower())
            db.insert_dependency(element.text.lower(),
                                 table_name, company_name)


scrape_dependencies()
