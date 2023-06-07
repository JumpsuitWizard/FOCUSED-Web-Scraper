from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import PANAPTO_URL
import re
from utils.database import Database
from utils.selenium import get_dynamic_html


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'panapto_dependencies'
    db.create_table(table_name)

    html_text = get_dynamic_html(PANAPTO_URL)

    soup = BeautifulSoup(html_text, 'lxml')

    elements = soup.select('body table > tbody > tr > td:nth-child(1)')
    for element in elements[1:]:
        print(element.text.strip())
        db.insert_dependency(element.text.strip(), table_name)


scrape_dependencies()
