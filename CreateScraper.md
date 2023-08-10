# BeautifulSoup and Requests Scraper Template

This template provides a basic structure for creating a web scraper using BeautifulSoup and requests. Replace the specific details such as target URL and database configurations with your desired values.

You need to add the company url in urls.py:

```bash
YOUR_COMPANY_URL = 'https://www.example.com'
```

# If the scraping doesn't need selenium then use the below template

```sh
    from bs4 import BeautifulSoup
    import requests
    from utils.database import Database
    from utils.utility import remove_at_symbol
    #import the url
    from config.urls import { YOUR_URL }


    def scrape_dependencies():

        # Replace 'YOUR_CONFIG_FILE_PATH' with the path to your database configuration file
        db = Database(config_file='config/db_config.json')
        db.read_config()
        db.connect()

        # Define the table name and company name for the database
        table_name = 'all_dependencies'
        company_name = '{ COMPANY_NAME }'

        # Create the database table (if not already exists)
        db.create_table(table_name)

        # Replace 'YOUR_SPOTIFY_URL' with the URL of the target website you want to scrape
        html_text = requests.get('{ URL }').text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_text, 'lxml')

        # Find all the dependencies in the HTML content
        # Use your own selector logic to target specific elements containing the dependencies
        dependencies = soup.find_all('div', class_='{ CLASS_NAME }')

        package_name_set = set()
        # Replace this logic with your specific scraping logic
        for element in dependencies:
            # Clean and extract the dependency name
            value = remove_at_symbol(element.text)

            # Check if the dependency name is not already in the set (to avoid duplicates)
            if value.lower() not in package_name_set:
                package_name_set.add(value.lower())

                # Insert the dependency into the database
                db.insert_dependency(value, table_name, company_name)

        # Close the database connection
        db.close_connection()

    # Call the function to run the scraper
    scrape_dependencies()

```

# If the scraping need selenium then use the below template

```sh
    from bs4 import BeautifulSoup
    import requests
    import psycopg2
    from config.urls import { YOUR_URL }
    import re
    from utils.database import Database
    from utils.selenium import get_dynamic_html
    from utils.utility import remove_at_symbol


    def scrape_dependencies():

        db = Database(config_file='config/db_config.json')
        db.read_config()
        db.connect()
        table_name = 'all_dependencies'
        company_name = 'meta ray ban'
        db.create_table(table_name)

        html_text = get_dynamic_html( { YOUR_URL } )

        soup = BeautifulSoup(html_text, 'lxml')

        # Find all the dependencies in the HTML content
        # Use your own selector logic to target specific elements containing the dependencies
        elements = soup.find_all('div', class_='{ CLASS_NAME }')

        package_name_set = set()

        for element in elements:
            if element.text.lower() not in package_name_set:
                value = remove_at_symbol(element.text.strip())
                package_name_set.add(value.lower())
                db.insert_dependency(value, table_name, company_name)


    scrape_dependencies()

```
