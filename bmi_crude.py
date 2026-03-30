# UPDATE - Update user's weight
def update_user_weight(name, new_weight):
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT height FROM bmi_records WHERE name = %s", (name,))
            result = cur.fetchone()

            if result:
                height = result[0]
                new_bmi = new_weight / (height * height)
                cur.execute("""
                            UPDATE bmi_records
                            SET weight = %s,
                                bmi    = %s
                            WHERE name = %s
                            """, (new_weight, new_bmi, name))
                print("weight updated successfully")
            else:
                print("user not found")


# DELETE - Delete user
def delete_user(name):
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM bmi_records WHERE name = %s", (name,))
            if cur.rowcount > 0:
                print("user deleted successfully")
            else:
                print("user not found")