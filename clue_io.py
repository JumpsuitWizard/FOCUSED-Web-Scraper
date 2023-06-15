from bs4 import BeautifulSoup
import requests
from config.urls import CLUE_IO_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'clueio_dependencies'
    db.create_table(table_name)

    html_text = requests.get(CLUE_IO_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    list_elements = soup.select('section .col-sm-4 ul > li')
    dependency_list = []

    for element in list_elements:
        dependency_list.append(element.text)

    table_elements = soup.select('table tr > td:nth-child(1)')
    for element in table_elements:
        dependency_list.append(element.text)

    for element in dependency_list:
        db.insert_dependency(element, table_name)


scrape_dependencies()
