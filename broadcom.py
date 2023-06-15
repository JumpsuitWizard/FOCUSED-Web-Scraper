from bs4 import BeautifulSoup
import requests
import psycopg2
from config.urls import BROADCOM_URL
import re
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'broadcom_dependencies'
    table_name = 'all_dependencies'
    company_name = 'broadcom'
    db.create_table(table_name)

    html_text = requests.get(BROADCOM_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select(
        '[id="concept.dita_7dbb24920dfa3a5dce2a5f99db97517299650986_KeyFeatures14.4"] .ul .li div')
    package_name_set = set()
    for package in elements:
        name = ""
        version = ""

        package_text = package.get_text(strip=True)
        version_match = re.search(
            r"(\bv?\d+(\.\d+)*\b)", package_text, re.IGNORECASE)
        if version_match:
            version = version_match.group(1)
            name = re.sub(r"(\bv?\d+(\.\d+)*\b)", "", package_text).strip()
        else:
            name = package_text
            version = None
        if name not in package_name_set:
            package_name_set.add(name)
            db.insert_dependency(name, table_name, company_name, version)


scrape_dependencies()
