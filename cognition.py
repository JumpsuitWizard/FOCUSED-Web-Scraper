from bs4 import BeautifulSoup
import requests
from config.urls import COGNITION_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'cognition_dependencies'
    table_name = 'all_dependencies'
    company_name = 'cognition'
    db.create_table(table_name)

    html_text = requests.get(COGNITION_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('section > div h3')
    package_name_set = set()
    for package_name in elements:
        if package_name.text.lower() not in package_name_set:
            package_name_set.add(package_name.text.lower())
            db.insert_dependency(package_name.text, table_name, company_name)


scrape_dependencies()
