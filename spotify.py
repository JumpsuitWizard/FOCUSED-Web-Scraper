from bs4 import BeautifulSoup
import requests
import psycopg2
from database import Database
from urls import SPOTIFY_URL


def create_connection():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='dependencies',
        port='5432'
    )
    return connection


def insert_dependency(package_name):
    connection = create_connection()
    cursor = connection.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS spotify_dependencies (
            id serial PRIMARY KEY,
            package_name character varying(255)
        )'''

    cursor.execute(create_table_query)

    insert_query = "INSERT INTO spotify_dependencies (package_name) VALUES (%s)"
    values = (package_name,)

    cursor.execute(insert_query, values)
    connection.commit()

    cursor.close()
    connection.close()


def scrape_dependencies():

    html_text = requests.get(SPOTIFY_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.find_all('div', class_='sc-589317f5-1 hPDpvs')
    dependency_list = []

    for index, value in enumerate(dependencies):
        package_name = value.text
        if index == 0 or index == 1:
            continue
        else:
            insert_dependency(package_name)


scrape_dependencies()
