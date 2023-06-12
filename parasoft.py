from bs4 import BeautifulSoup
import requests
from config.urls import PARASOFT_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'parasoft_dependencies'
    db.create_table(table_name)

    html_text = requests.get(PARASOFT_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#main-content > p > strong')
    print(elements)
    for element in elements[1:]:
        db.insert_dependency(element.text, table_name)


scrape_dependencies()
