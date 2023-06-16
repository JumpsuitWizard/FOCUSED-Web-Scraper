from bs4 import BeautifulSoup
import requests
from config.urls import ORACLE_FUSION_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'oracle_fusion_dependencies'
    table_name = 'all_dependencies'
    company_name = 'oracle fusion'
    db.create_table(table_name)

    html_text = requests.get(ORACLE_FUSION_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('article > div > div:nth-child(2) > ul > li > a')

    package_name_set = set()

    for element in elements:
        if element.text.lower() not in package_name_set:
            value = remove_at_symbol(element.text.strip())
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
