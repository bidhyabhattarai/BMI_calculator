total_users = int(input("How many user data do you want to enter?"))
user_data = []
for i in range(total_users):
    print(f"\nEntering data for user {i + 1}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    health_tags = input("Enter health tags (comma-separated): ").split(",")
    user_data.append({ # Storing user data in a dictionary
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "health_tags": health_tags
    })

# print user data
for user in user_data:
    print(f"Name: {user['name']}, Age: {user['age']}, Height: {user['height']} m, Weight: {user['weight']} kg, Health Tags: {', '.join(user['health_tags'])}")
