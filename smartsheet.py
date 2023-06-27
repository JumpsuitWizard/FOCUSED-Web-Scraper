from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import SMARTSHEET_URL
import re
from utils.utility import remove_at_symbol
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'smartsheet_dependencies'
    table_name = 'all_dependencies'
    company_name = 'smartsheet'
    db.create_table(table_name)

    # Added this header to mimic browser
    html_text = requests.get(SMARTSHEET_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    lines = []
    prev_line = None

    package_name_set = set()

    for line in soup.stripped_strings:
        if line.startswith('https'):
            if prev_line is not None:
                lines.append(prev_line)
            prev_line = None
        else:
            prev_line = line

    for package in lines:
        if package.lower() not in package_name_set:
            value = remove_at_symbol(package)
            package_name_set.add(package.lower())
            db.insert_dependency(value, table_name,
                                 company_name)


scrape_dependencies()
