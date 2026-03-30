# db_connect.py
import psycopg2
from psycopg2 import Error
from db_config import DB_CONFIG


def get_connection():

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✓ Connected to PostgreSQL database successfully!")
        return conn
    except Error as e:
        print(f"✗ Error connecting to database: {e}")
        return None


def close_connection(conn):
   
    if conn:
        conn.close()
        print("✓ Database connection closed")


def test_connection():

    conn = get_connection()
    if conn:
        close_connection(conn)
        return True
    return False


# Test connection when script runs directly
if __name__ == "__main__":
    print("Testing database connection...")
    if test_connection():
        print("✓ Database connection test PASSED")
    else:
        print("✗ Database connection test FAILED")