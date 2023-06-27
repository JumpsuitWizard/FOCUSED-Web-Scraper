from bs4 import BeautifulSoup
import requests
import psycopg2
from utils.database import Database
from utils.utility import remove_at_symbol
from config.urls import SPOTIFY_URL


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'spotify_dependencies'
    table_name = 'all_dependencies'
    company_name = 'spotify'
    db.create_table(table_name)

    html_text = requests.get(SPOTIFY_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.find_all('div', class_='sc-589317f5-1 hPDpvs')
    dependency_list = []

    package_name_set = set()

    for element in dependencies[2:]:
        if element.text.lower() not in package_name_set:
            value = remove_at_symbol(element.text)
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
