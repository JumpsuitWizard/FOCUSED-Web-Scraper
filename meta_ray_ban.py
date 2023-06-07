from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import META_RAY_BAN
import re
from utils.database import Database
from utils.selenium import get_dynamic_html


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'meta_ray_ban_dependencies'
    db.create_table(table_name)

    html_text = get_dynamic_html(META_RAY_BAN)

    soup = BeautifulSoup(html_text, 'lxml')

    elements = soup.select('body div p span.x117nqv4')

    for element in elements:
        db.insert_dependency(element.text, table_name)


scrape_dependencies()
