from bs4 import BeautifulSoup
import requests
import re
from config.urls import VEERTU_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'parasoft_dependencies'
    table_name = 'all_dependencies'
    company_name = 'veertu'
    db.create_table(table_name)

    html_text = requests.get(VEERTU_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    p_tags = soup.find_all('p')
    package_name_set = set()
    for p_tag in p_tags:
        a_tag = p_tag.find('a', href=re.compile('^https://'))
        if a_tag:
            text_parts = [
                part for part in p_tag.contents if isinstance(part, str)]
            text = ' '.join(text_parts).strip()
            package_names = re.findall(r'^\w+:$', text, re.MULTILINE)
            package_names = [name.rstrip(':') for name in package_names]
            package_name_set.update(package_names)

    for package_name in package_name_set:
        db.insert_dependency(package_name, table_name, company_name)


scrape_dependencies()
