from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from utils.database import Database
from utils.utility import remove_at_symbol
from config.urls import SLACK_URL


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'slack_dependencies'
    table_name = 'all_dependencies'
    company_name = 'slack'
    db.create_table(table_name)

    html_text = requests.get(SLACK_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.find_all('div', class_='card')
    package_name_set = set()

    for index, dependency in enumerate(dependencies):
        dependency_list = dependency.h3.a.text.split(' ')
        package_name = dependency_list[0]
        package_version = dependency_list[1][1:-1]

        declared_licenses_element = dependency.find(
            'div', class_='dependency__declared-licenses')
        if declared_licenses_element:
            declared_licenses = declared_licenses_element.text.replace(' ', '')

        discovered_licenses_element = dependency.find(
            'div', class_='dependency__discovered-licenses')
        if discovered_licenses_element:
            discovered_licenses = discovered_licenses_element.text.replace(
                ' ', '')

        pre_element = dependency.find('div', class_='show-more').pre
        pre_element.button.extract()
        copyright_info = pre_element.text.strip()
        MAX_LENGTH = 100
        if len(copyright_info) > MAX_LENGTH:
            shortened_copyright_info = f"{copyright_info[:MAX_LENGTH]}..."
        else:
            shortened_copyright_info = copyright_info

        if package_name.lower() not in package_name_set:
            value = remove_at_symbol(package_name)
            package_name_set.add(package_name.lower())
            db.insert_dependency(value, table_name,
                                 company_name, package_version)


scrape_dependencies()
