from bs4 import BeautifulSoup
import requests
from config.urls import SPARK_TRADER_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'spark_trader_dependencies'
    table_name = 'all_dependencies'
    company_name = 'spark trader'
    db.create_table(table_name)

    html_text = requests.get(SPARK_TRADER_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#top ul > li > a')

    package_name_set = set()

    for element in elements:
        if element.text.lower() not in package_name_set:
            value = remove_at_symbol(element.text)
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
