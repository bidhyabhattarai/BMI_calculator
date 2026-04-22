import psycopg2
from dbconnect import get_connection

# connection to db
conn = get_connection()
print("Connected to database")

# bmi calculation function
def calculate_bmi(weight, height):
    return weight / (height * height)

# create table
def create_table():
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS bmi_records (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    weight REAL,
                    height REAL,
                    bmi REAL
                )
            """)
    print("Table ready")

create_table()

# insert
def insert_data(name, weight, height):
    bmi = calculate_bmi(weight, height)

    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO bmi_records (name, weight, height, bmi)
                VALUES (%s, %s, %s, %s)
            """, (name, weight, height, bmi))

    print(f"Data inserted successfully | BMI = {bmi:.2f}")

# fetch
def fetch_data():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM bmi_records")
            rows = cur.fetchall()

    print("\n--- BMI Records ---")
    for row in rows:
        id, name, weight, height, bmi = row
        print(f"ID: {id} | Name: {name} | Weight: {weight} | Height: {height} | BMI: {bmi:.2f}")

# update
def update_data(record_id, weight, height):
    bmi = calculate_bmi(weight, height)

    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE bmi_records
                SET weight = %s,
                    height = %s,
                    bmi = %s
                WHERE id = %s
            """, (weight, height, bmi, record_id))

    print(f"Record updated successfully | New BMI = {bmi:.2f}")

# delete
def delete_data(record_id):
    # fetch record before deleting (to show user)
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM bmi_records WHERE id = %s", (record_id,))
            row = cur.fetchone()

    if row:
        name = row[0]

        with conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM bmi_records WHERE id = %s", (record_id,))

        print(f"Record of '{name}' deleted successfully")
    else:
        print("Record not found!")

# menu
def menu():
    while True:
        print("\n===== BMI APP MENU =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            insert_data(name, weight, height)

        elif choice == "2":
            fetch_data()

        elif choice == "3":
            record_id = int(input("Enter ID to update: "))
            weight = float(input("Enter new weight: "))
            height = float(input("Enter new height: "))
            update_data(record_id, weight, height)

        elif choice == "4":
            record_id = int(input("Enter ID to delete: "))
            delete_data(record_id)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

menu()