from bs4 import BeautifulSoup
import requests
from config.urls import APPLE_MAPS_URL
import re
from utils.database import Database


def scrape_dependencies():

    db = Database(config_file='config/db_config.json')
    db.read_config()
    db.connect()
    table_name = 'all_dependencies'
    company_name = 'apple maps'
    db.create_table(table_name)

    html_text = requests.get(APPLE_MAPS_URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    elements = soup.select('p')
    selected_elements = []
    for element in elements:
        next_element = element.find_next_sibling('p')
        if next_element and 'Copyright' in next_element.text:
            b_tag = element.find('b')
            if b_tag:
                selected_elements.append(b_tag.text)

    for package in selected_elements:
        matches = re.findall(r'\((.*?)\)', package)
        if matches:
            extracted_content = matches[0]
            db.insert_dependency(extracted_content, table_name, company_name)


scrape_dependencies()
