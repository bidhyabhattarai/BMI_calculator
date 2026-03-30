import psycopg2
from dbconnect import get_connection

#connection establish
conn = get_connection()
print("Connected to database")

#create table if not exists
def create_table():
    with conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS bmi_records (
                                id SERIAL PRIMARY KEY,
                                name varchar(255),
                                weight real,
                                height real,
                                bmi real
                           )
                        """)
            print("table created successfully")

create_table()

