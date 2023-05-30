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
            print(config)
            self.host = config.get('host')
            self.user = config.get('user')
            self.password = config.get('password')
            self.database = config.get('database')
            self.port = config.get('port')

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def close(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id serial PRIMARY KEY,
                package_name character varying(255),
                package_version character varying(255)
            )'''

        cursor = self.connection.cursor()
        cursor.execute(create_table_query)
        cursor.close()


    def insert_dependency(self, package_name, package_version=None):
        insert_query = "INSERT INTO porsche_dependencies (package_name, package_version) VALUES (%s, %s)"
        values = (package_name, package_version)

        cursor = self.connection.cursor()
        cursor.execute(insert_query, values)
        self.connection.commit()
        cursor.close()
