import sys
sys.path.append('..')
import requests
import pdfplumber
from bs4 import BeautifulSoup
import os
from slackopen import urls
import re
import psycopg2



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
        CREATE TABLE IF NOT EXISTS adobe_dependencies (
            id serial PRIMARY KEY,
            package_name character varying(255)
        )'''

    cursor.execute(create_table_query)

    insert_query = "INSERT INTO adobe_dependencies (package_name) VALUES (%s)"
    values = (package_name,)

    cursor.execute(insert_query, values)
    connection.commit()

    cursor.close()
    connection.close()


def download_pdf(url, file_name):
    response = requests.get(url)
    # Gets the absolute path of the current script
    base_path = os.path.dirname(os.path.abspath(__file__))  
    # Creating the full path by joining the base path and file name
    file_path = os.path.join(base_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)


response = requests.get(urls.ADOBE_URL)
soup = BeautifulSoup(response.content, 'html.parser')

pdf_links_div = soup.find('div', {'id': 'root_content_flex'})
pdf_link_href = pdf_links_div.find_all('a',href=True)

    
# Download each PDF file and extract its text content
unique_dependencies = set()

# for index, link in enumerate(pdf_link_href, start=1):
#     href = link['href']   
#     if 'pdf' in href.lower():
#         if href.startswith('https'):
#             pdf_url = href
#         else:
#             pdf_url = f"https://www.adobe.com{href}"

#         pdf_file_name =  f'pdf{index}.pdf'
#         download_pdf(pdf_url, pdf_file_name) 


with pdfplumber.open(f"adobe/pdf31.pdf") as pdf:
    text = ''
    for page in pdf.pages:
        text+=page.extract_text()

    lines = text.split('\n')
    print(lines)
    dependencies = []
    for i, line in enumerate(lines):
        if line.startswith("ID:") and i > 0:
            dependency = lines[i-1].replace("_", "")
            
            # Remove numbers from the dependency
            # As it is also considering page number in some of the dependencies
            dependency = re.sub(r'\d+', '', dependency)
            if ':/' in dependency:
                continue
            else:
                dependencies.append(dependency.strip())
    print(dependencies)
    for value in dependencies:
        if value not in unique_dependencies:
            # insert_dependency(value)
            # print(value)
            unique_dependencies.add(value)
        