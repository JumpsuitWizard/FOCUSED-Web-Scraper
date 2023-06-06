from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import SMARTSHEET_URL
import re
from utils.database import Database

def connect_db(table_name):
    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    db.create_table(table_name)

def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'smartsheet_dependencies'
    db.create_table(table_name)

    # Added this header to mimic browser
    html_text = requests.get(SMARTSHEET_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    lines=[]
    prev_line = None

    for line in soup.stripped_strings:
        if line.startswith('https'):
            if prev_line is not None:
                lines.append(prev_line)
            prev_line = None
        else:
            prev_line = line

    for package in lines:
        db.insert_dependency(package, table_name)

scrape_dependencies()