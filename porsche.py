from bs4 import BeautifulSoup
import requests
import psycopg2
import re
from urls import PORSCHE_URL

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
        CREATE TABLE IF NOT EXISTS porsche_dependencies (
            id serial PRIMARY KEY,
            package_name character varying(255)
        )'''

    cursor.execute(create_table_query)

    insert_query = "INSERT INTO porsche_dependencies (package_name) VALUES (%s)"
    values = (package_name,)

    cursor.execute(insert_query, values)
    connection.commit()

    cursor.close()
    connection.close()


def scrape_dependencies():
    html_text = requests.get(PORSCHE_URL).text

    pattern = r'(?<=\*{5}\n)(.*?)(?=\n\*{5})'

    dependencies = re.findall(pattern, html_text)

    for index, value in enumerate(dependencies):
        insert_dependency(value)

scrape_dependencies()