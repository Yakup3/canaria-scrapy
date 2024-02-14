import psycopg2
from jobs_project.database import Database

class PostgreSQLPipeline:
    def __init__(self, postgres_host, postgres_port, postgres_user, postgres_password, postgres_db):
        self.db = Database(
            dbname=postgres_db,
            user=postgres_user,
            password=postgres_password,
            host=postgres_host,
            port=postgres_port
        )
        self.db.connect()

        self.db.create_table(create_table_file='jobs_project/create_table.sql')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            postgres_host=crawler.settings.get('POSTGRES_HOST'),
            postgres_port=crawler.settings.get('POSTGRES_PORT'),
            postgres_user=crawler.settings.get('POSTGRES_USER'),
            postgres_password=crawler.settings.get('POSTGRES_PASSWORD'),
            postgres_db=crawler.settings.get('POSTGRES_DB')
        )

    def close_spider(self, spider):
        self.db.close_connection()

    def process_item(self, item, spider):
        try:
            success = Database.insert_record(self.db.connection, self.db.cursor, 'raw_table', item)
            if success:
                print("Record inserted successfully into raw_table", item['slug'])
            else:
                print("Failed to insert record into raw_table")
        except psycopg2.Error as e:
            print("Error inserting item:", e)
        return item