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

def insert_data(name, weight, height):
    bmi = weight / (height * height)

    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO bmi_records (name, weight, height, bmi)
                VALUES (%s, %s, %s, %s)
            """, (name, weight, height, bmi))
            print("data inserted successfully")

def fetch_data():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM bmi_records")
            rows = cur.fetchall()

            print("\n--- BMI Records ---")
            for row in rows:
                print(row)

