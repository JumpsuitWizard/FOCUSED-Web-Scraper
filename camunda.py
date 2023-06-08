from bs4 import BeautifulSoup
import requests
from config.urls import CAMUNDA_URL
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'camunda_dependencies'
    db.create_table(table_name)

    html_text = requests.get(CAMUNDA_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.find('h1', id='java-dependencies')
    div_elements = dependencies.find_next_siblings('div')

    for div in div_elements:
        package = div.find('summary').text.split('(')[0]
        last_at_index = package.rindex('@')
        package_name, version_number = package[:
                                               last_at_index], package[last_at_index + 1:]
        db.insert_dependency(package_name, table_name, version_number)


scrape_dependencies()
