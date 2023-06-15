from bs4 import BeautifulSoup
import requests
from config.urls import NVIDIA_URL
from utils.database import Database

# NVIDIA TAO TOOLKIT


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'nvidia_dependencies'
    db.create_table(table_name)

    html_text = requests.get(NVIDIA_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('.StepModuleHeader-anchorLink')
    for element in elements:
        db.insert_dependency(element.text, table_name)


scrape_dependencies()
