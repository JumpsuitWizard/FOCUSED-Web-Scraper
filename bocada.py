from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import BOCADA_URL
import re
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'bocada_dependencies'
    db.create_table(table_name)

    html_text = requests.get(BOCADA_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#post-3789 p > strong')
    for element in elements:
        db.insert_dependency(element.text, table_name)


scrape_dependencies()
