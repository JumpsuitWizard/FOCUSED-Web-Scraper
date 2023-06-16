from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import BOSCH_URL
import re
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'all_dependencies'
    company_name = 'bosch'
    db.create_table(table_name)

    # Added this header to mimic browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    html_text = requests.get(BOSCH_URL, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    # regex way
    # lines = soup.find_all(string=lambda text: re.search(r'^@{1,2}\w+', text))

    lines = [line for line in soup.stripped_strings if line.startswith('@')]

    for line in lines:
        parts = line.rsplit(' - ', 1)
        if len(parts) == 2:
            package_name, version = parts
            package = remove_at_symbol(package_name.strip(
            ))
            db.insert_dependency(package, table_name,
                                 company_name, version.split(":")[1])


scrape_dependencies()
