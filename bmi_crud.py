import psycopg2

#connection establish
conn = psycopg2.connect(
    user="postgres",
    password="bikita",
    host="localhost",
    port="5432",
    database="bmidb"
)
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

