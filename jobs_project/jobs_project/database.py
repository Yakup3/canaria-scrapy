import psycopg2
from psycopg2.extras import Json

class Database:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                database=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database.")
        except psycopg2.Error as e:
            print("Error connecting to the database:", e)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def create_table(self, create_table_file):
        try:
            with open(create_table_file, 'r') as f:
                create_table_query = f.read()

            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Table 'raw_table' created successfully.")
        except psycopg2.Error as e:
            print("Error creating table:", e)
            self.connection.rollback()
    
    def insert_record(connection, cursor, table_name, item):
        try:
            for key, value in item.items():
                if isinstance(value, dict) or isinstance(value, list):
                    item[key] = Json(value)

            columns = ", ".join(item.keys())
            values = ", ".join(["%s"] * len(item))
            
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

            record_to_insert = tuple(item.values())

            cursor.execute(insert_query, record_to_insert)
            connection.commit()
            return True
        except psycopg2.Error as e:
            print("Error inserting record:", e)
            connection.rollback()
            return False