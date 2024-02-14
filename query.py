import psycopg2
import csv

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

    def retrieve_data(self, table_name, output_file):
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([desc[0] for desc in self.cursor.description])
                writer.writerows(rows)
            print(f"Data retrieved and saved to {output_file}")
        except psycopg2.Error as e:
            print("Error retrieving data:", e)

if __name__ == "__main__":
    db = Database(dbname='canaria', user='postgres', password='1234', host='localhost', port=54321)
    db.connect()
    db.retrieve_data(table_name='raw_table', output_file='raw_table_output.csv')
    db.close_connection()
