from bs4 import BeautifulSoup
import requests
import psycopg2
from utils.database import Database
from config.urls import SPACETI_URL
from utils.selenium import get_dynamic_html
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'spaceti_dependencies'
    table_name = 'all_dependencies'
    company_name = 'spaceti'
    db.create_table(table_name)

    html_text = get_dynamic_html(SPACETI_URL)
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.select(
        '#content > app-support-license ul > li > a')
    dependency_list = []
    package_name_set = set()

    for element in dependencies:
        print(element.text)
        if element.text.lower() not in package_name_set:
            package_name_set.add(element.text.lower())
            db.insert_dependency(element.text.lower(),
                                 table_name, company_name)


scrape_dependencies()
