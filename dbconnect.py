import psycopg2

try:
    conn = psycopg2.connect(
        dbname='bim_db',      # your database name
        user='enzeladb',       # the user you created
        password='test123',    # the password you set
        host='localhost',      # PostgreSQL is on your machine
        port=5432              # default PostgreSQL port
    )

    cur = conn.cursor()
    cur.execute("SELECT version();")  # just to test connection
    print("Connected to:", cur.fetchone())

    # your further database operations go here

    cur.close()
    conn.close()

except Exception as e:
    print("Connection failed:", e)