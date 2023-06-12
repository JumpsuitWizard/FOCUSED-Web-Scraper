from bs4 import BeautifulSoup
import requests
from config.urls import BOX_URL
from utils.database import Database


def scrape_dependencies():
    # has some duplicate dependencies
    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'box_dependencies'
    db.create_table(table_name)

    html_text = requests.get(BOX_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('article > p > b')
    for element in elements:
        package = element.text
        if ':' in package:
            package_name = package.split(':')[0]
            db.insert_dependency(package_name, table_name)


scrape_dependencies()
