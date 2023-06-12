from bs4 import BeautifulSoup
import requests
from config.urls import ORACLE_FUSION_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'oracle_fusion_dependencies'
    db.create_table(table_name)

    html_text = requests.get(ORACLE_FUSION_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('article > div > div:nth-child(2) > ul > li > a')

    for element in elements:
        db.insert_dependency(element.text, table_name)


scrape_dependencies()
