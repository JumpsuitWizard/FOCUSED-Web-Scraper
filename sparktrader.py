from bs4 import BeautifulSoup
import requests
from config.urls import SPARK_TRADER_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'spark_trader_dependencies'
    db.create_table(table_name)

    html_text = requests.get(SPARK_TRADER_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#top ul > li > a')
    for element in elements:
        db.insert_dependency(element.text, table_name)


scrape_dependencies()
