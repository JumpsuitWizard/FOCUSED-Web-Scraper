from bs4 import BeautifulSoup
import requests
from config.urls import ADLOCK_URL
from utils.database import Database
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable the warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'all_dependencies'
    company_name = 'adlock'
    db.create_table(table_name)

    html_text = requests.get(ADLOCK_URL, verify=False).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#page2945 > div > p > b')

    for i, element in enumerate(elements):
        text = element.get_text(strip=True)
        if text:
            db.insert_dependency(text, table_name, company_name)


scrape_dependencies()
