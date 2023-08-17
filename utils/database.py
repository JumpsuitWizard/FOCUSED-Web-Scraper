import json
import psycopg2


class Database:
    def __init__(self, config_file):
        self.config_file = config_file
        self.connection = None
        self.host = None
        self.user = None
        self.password = None
        self.database = None
        self.port = None

    def read_config(self):
        with open(self.config_file) as f:
            config = json.load(f)
            self.host = config.get('host')
            self.user = config.get('user')
            self.password = config.get('password')
            self.database = config.get('database')
            self.port = config.get('port')

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            return self.connection

        except (psycopg2.Error, Exception) as error:
            print("Error connecting to the PostgreSQL database:", error)
            return None

    def close(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id serial PRIMARY KEY,
                company_name character varying(255),
                package_name character varying(255),
                package_version character varying(255)
            )'''

        cursor = self.connection.cursor()
        cursor.execute(create_table_query)
        cursor.close()

    def insert_dependency(self, package_name, table_name, company_name, package_version=None):
        select_query = f"SELECT id FROM {table_name} WHERE company_name = %s AND package_name = %s"
        select_values = (company_name, package_name)

        cursor = self.connection.cursor()
        cursor.execute(select_query, select_values)
        existing_row = cursor.fetchone()

        if not existing_row:
            insert_query = f"INSERT INTO {table_name} (company_name, package_name, package_version) VALUES (%s, %s, %s)"
            insert_values = (company_name, package_name, package_version)

            cursor.execute(insert_query, insert_values)
            self.connection.commit()
            print("Data inserted successfully.")
        else:
            print("Data already exists, not inserting.")

        cursor.close()
