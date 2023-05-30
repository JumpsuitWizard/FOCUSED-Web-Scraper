from bs4 import BeautifulSoup
import requests
import psycopg2
from urls import SAMSUNG_URL


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
        CREATE TABLE IF NOT EXISTS samsung_dependencies (
            id serial PRIMARY KEY,
            package_name character varying(255)
        )'''

    cursor.execute(create_table_query)

    insert_query = "INSERT INTO samsung_dependencies (package_name) VALUES (%s)"
    values = (package_name,)

    cursor.execute(insert_query, values)
    connection.commit()

    cursor.close()
    connection.close()



def scrape_dependencies():
    html_text = requests.get(SAMSUNG_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    # Select elements using CSS selectors
    elements = soup.select('#el-main-container tr > td:nth-child(2) > a')

    # Iterate over the selected elements
    for package in elements:
        # Perform operations on each element
        insert_dependency(package.text)

scrape_dependencies()