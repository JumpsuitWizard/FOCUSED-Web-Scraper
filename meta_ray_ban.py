from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import META_RAY_BAN
import re
from utils.database import Database
from utils.selenium import get_dynamic_html
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'meta_ray_ban_dependencies'
    table_name = 'all_dependencies'
    company_name = 'meta ray ban'
    db.create_table(table_name)

    html_text = get_dynamic_html(META_RAY_BAN)

    soup = BeautifulSoup(html_text, 'lxml')

    elements = soup.select('body div p span.x117nqv4')

    package_name_set = set()

    for element in elements:
        if element.text.lower() not in package_name_set:
            value = remove_at_symbol(element.text.strip())
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
