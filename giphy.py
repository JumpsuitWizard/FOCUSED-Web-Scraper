from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from utils.database import Database
from config.urls import GIPHY_URL
from utils.selenium import get_dynamic_html
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'giphy_dependencies'
    table_name = 'all_dependencies'
    company_name = 'giphy'
    db.create_table(table_name)

    html_text = get_dynamic_html(GIPHY_URL)
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.select(
        "section.article-info > div > div.article-body > p:nth-child(n+5):not(.wysiwyg-indent1)")
    pattern = r'^(.*?) \((.*?)\)$'

    package_name_set = set()

    for p_tag in dependencies[:-1]:
        package_name = p_tag.text.split('Copyright')[0]
        match = re.search(pattern, package_name, re.MULTILINE)
        if match:
            name = match.group(1)
            version = match.group(2)
            if name.lower() not in package_name_set:
                package_name_set.add(name.lower())
                db.insert_dependency(
                    name.lower(), table_name, company_name, version)


scrape_dependencies()
