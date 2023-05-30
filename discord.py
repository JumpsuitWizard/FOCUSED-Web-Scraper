from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from urls import DISCORD_URL

def create_connection():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='dependencies',
        port= '5432'
    )
    return connection


def insert_dependency(package_name):
    connection = create_connection()
    cursor = connection.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS discord_dependencies (
            id serial PRIMARY KEY,
            package_name character varying(255)
        )'''

    cursor.execute(create_table_query)

    insert_query = "INSERT INTO discord_dependencies (package_name) VALUES (%s)"
    values = (package_name,)

    cursor.execute(insert_query, values)
    connection.commit()

    cursor.close()
    connection.close()


def scrape_dependencies():
    html_text = requests.get(DISCORD_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

        # Search for the specific text
    target_text = "The following software may be included in this product:"
    matching_element = soup.find_all(lambda tag: tag.name == 'span' and target_text in tag.text)
    dependency_list = []
    for index, value in enumerate(matching_element):
        dependency = value.text.split(':')[1].split('.')[0]
        if "," in dependency:
            dependency_list.extend(dependency.split(","))
        else:
            dependency_list.append(dependency)
    for package_name in dependency_list:
        print(package_name)
        insert_dependency(package_name.strip())

scrape_dependencies()