import psycopg2
from dbconnect import get_connection


conn = get_connection()
print("Connected to database")


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
            print("Table created successfully")


create_table()


# ============================================
# UPDATE - Update user's weight
# ============================================

def update_user_weight(name, new_weight):
    """Update user's weight and recalculate BMI"""
    with conn:
        with conn.cursor() as cur:
            # Get user's height
            cur.execute("SELECT height FROM bmi_records WHERE name = %s", (name,))
            result = cur.fetchone()

            if result:
                height = result[0]
                # Calculate new BMI
                new_bmi = round(new_weight / (height ** 2), 2)

                # Update
                cur.execute("""
                    UPDATE bmi_records 
                    SET weight = %s, bmi = %s 
                    WHERE name = %s
                """, (new_weight, new_bmi, name))

                print(f"✓ Updated {name}: weight={new_weight}kg, BMI={new_bmi}")
            else:
                print(f"✗ User '{name}' not found")


# ============================================
# DELETE - Delete user
# ============================================

def delete_user(name):
    """Delete user by name"""
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM bmi_records WHERE name = %s", (name,))
            if cur.rowcount > 0:
                print(f"✓ Deleted user '{name}'")
            else:
                print(f"✗ User '{name}' not found")


