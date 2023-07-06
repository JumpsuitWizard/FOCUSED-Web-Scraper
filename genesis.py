from bs4 import BeautifulSoup
import requests
import re
from config.urls import GENESIS_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'parasoft_dependencies'
    table_name = 'all_dependencies'
    company_name = 'genesis'
    db.create_table(table_name)

    html_text = requests.get(GENESIS_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('#table-1 > tbody > tr > td.x3col-L > p')
    package_name_set = set()

    for package_name in elements:
        package_name_text = package_name.find(
            string=True, recursive=False).strip()
        match = re.match(r'^(.*?)\s+(\d+(?:\.\d+)+)$', package_name_text)
        if match:
            package_name_part = match.group(1)
            version_number = match.group(2)
            if package_name_part.lower() not in package_name_set:
                package_name_set.add(package_name_part.lower())
                db.insert_dependency(
                    package_name_part, table_name, company_name, version_number)
        else:
            continue


scrape_dependencies()
