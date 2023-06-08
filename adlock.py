from bs4 import BeautifulSoup
import requests
from config.urls import ADLOCK_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'adlock_dependencies'
    db.create_table(table_name)

    html_text = requests.get(ADLOCK_URL, verify=False).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#page2945 > div > p > b')

    for i, element in enumerate(elements):
        text = element.get_text(strip=True)
        if text:
            db.insert_dependency(text, table_name)


scrape_dependencies()
