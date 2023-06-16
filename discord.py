from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from config.urls import DISCORD_URL
from utils.database import Database
from utils.utility import remove_at_symbol


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    # table_name = 'confluent_dependencies'
    table_name = 'all_dependencies'
    company_name = 'discord'
    db.create_table(table_name)

    html_text = requests.get(DISCORD_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    # Search for the specific text
    target_text = "The following software may be included in this product:"
    matching_element = soup.find_all(
        lambda tag: tag.name == 'span' and target_text in tag.text)
    dependency_list = []
    for index, value in enumerate(matching_element):
        dependency = value.text.split(':')[1].split('.')[0]
        if "," in dependency:
            dependency_list.extend(dependency.split(","))
        else:
            dependency_list.append(dependency)

    package_name_set = set()

    for package_name in dependency_list:
        if package_name.lower() not in package_name_set:
            package_name_set.add(package_name.lower())
            value = remove_at_symbol(package_name.strip())
            db.insert_dependency(value,
                                 table_name, company_name)


scrape_dependencies()
