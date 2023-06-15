from bs4 import BeautifulSoup
import requests
from config.urls import BOCADA_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'all_dependencies'
    company_name = 'bocada'
    db.create_table(table_name)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    html_text = requests.get(BOCADA_URL, headers=headers).text

    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#post-3789 p > strong')

    for element in elements:
        db.insert_dependency(element.text, table_name, company_name)


scrape_dependencies()
