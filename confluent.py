from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import CONFLUENT_URL
import re
from utils.database import Database

def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'confluent_dependencies'
    db.create_table(table_name)

    html_text = requests.get(CONFLUENT_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#t01 > tbody > tr > td:nth-child(1)')
    for package in elements[1:]:
        db.insert_dependency(package.text, table_name)

scrape_dependencies()