from bs4 import BeautifulSoup
import requests
import psycopg2
from urls import SLACK_URL

def create_connection():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='dependencies',
        port= '5432'
    )
    return connection


def insert_dependency(package_name, package_version):
    connection = create_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO package_dependencies (package_name, package_version) VALUES (%s, %s)"
    values = (package_name, package_version)

    cursor.execute(insert_query, values)
    connection.commit()

    cursor.close()
    connection.close()


def scrape_dependencies():
    html_text = requests.get(SLACK_URL).text
    soup = BeautifulSoup(html_text, 'lxml')

    dependencies = soup.find_all('div', class_='card')
    for index, dependency in enumerate(dependencies):
        dependency_list = dependency.h3.a.text.split(' ')
        package_name = dependency_list[0]
        package_version = dependency_list[1][1:-1]

        declared_licenses_element = dependency.find('div', class_='dependency__declared-licenses')
        if declared_licenses_element:
            declared_licenses = declared_licenses_element.text.replace(' ', '')
            print('Declared licenses:', declared_licenses.strip())

        discovered_licenses_element = dependency.find('div', class_='dependency__discovered-licenses')
        if discovered_licenses_element:
            discovered_licenses = discovered_licenses_element.text.replace(' ', '')
            print('Discovered licenses:', discovered_licenses.strip())

        pre_element = dependency.find('div', class_='show-more').pre
        pre_element.button.extract()
        copyright_info = pre_element.text.strip()
        MAX_LENGTH = 100
        if len(copyright_info) > MAX_LENGTH:
            shortened_copyright_info = f"{copyright_info[:MAX_LENGTH]}..."
        else:
            shortened_copyright_info = copyright_info
        
        insert_dependency(package_name, package_version)

scrape_dependencies()