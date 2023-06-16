from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from config.urls import SAMSUNG_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'parasoft_dependencies'
    table_name = 'all_dependencies'
    company_name = 'samsung'
    db.create_table(table_name)

    html_text = requests.get(SAMSUNG_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    elements = soup.select('#el-main-container tr > td:nth-child(1) > a')
    package_name_set = set()
    license_td = soup.find_all('td', rowspan=True)
    for package in license_td:
        package_name = package.find_next_sibling('td').text.strip()
        if package_name.lower() not in package_name_set:
            value = remove_at_symbol(package_name)
            package_name_set.add(value)
    other_trs = [tr for tr in soup.find_all('tr') if not any(
        td.get('rowspan') for td in tr.find_all('td'))]
    other_second_td_list = [tr.find_all('td')[0] for tr in other_trs[1:]]

    for element in other_second_td_list:
        if element.text.lower() not in package_name_set:
            value = remove_at_symbol(element.text.strip())
            package_name_set.add(value.lower())
            db.insert_dependency(value, table_name, company_name)


scrape_dependencies()
