from bs4 import BeautifulSoup
import requests
import psycopg2
from urls import CISCO_URL
import re
from database import Database

def scrape_dependencies():

    db = Database(config_file='db_config.json')
    db.read_config()
    db.connect()
    table_name = 'cisco_dependencies'
    db.create_table(table_name)


    html_text = requests.get(CISCO_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    dependency_list = []
    elements = soup.select('.pBu1_Bullet1 a')
    for value in elements:
        # Handling the case where the dependency name are concatenated with and 
        if 'and' in value.text:
            names = value.text.split('and')
            dependency_list.extend(names)
        else:
            dependency_list.extend(value)


    for package in dependency_list:
        name = ""
        version = ""
            
        version_match = re.search(r"(\bv?\d+(\.\d+)*\b)", package, re.IGNORECASE)
        if version_match:
            version = version_match.group(1)
            name = package.replace(version, "").strip()
        else:
            name = package.strip()
            version = None

        db.insert_dependency(name, table_name, version)

scrape_dependencies()