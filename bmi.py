total_users = int(input("How many user data do you want to enter?"))
user_data = []
all_health_conditions = set()  # Set to store unique health conditions
for i in range(total_users):
    print(f"\nEntering data for user {i + 1}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    health_tags = input("Enter health tags (comma-separated): ").split(",")

    health_tags = [tag.strip() for tag in health_tags]  # Clean spaces
    all_health_conditions.update(health_tags)  # Add to set

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


underweight = (0, 18.5)
normal = (18.5, 24.9)
overweight = (25, 29.9)
obese = (30, float('inf'))

for user in user_data:
    height = user["height"]
    weight = user["weight"]

    # Avoid division by zero
    if height == 0:
        user["bmi"] = 0
        user["category"] = "Invalid"
        continue

    bmi = weight / (height * height)
    user["bmi"] = round(bmi, 2)

    if underweight[0] <= bmi < underweight[1]:
        category = "Underweight"
    elif normal[0] <= bmi < normal[1]:
        category = "Normal"
    elif overweight[0] <= bmi < overweight[1]:
        category = "Overweight"
    else:
        category = "Obese"

    user["category"] = category

for user in user_data:
    print(f"Name: {user['name']}, Age: {user['age']}, BMI: {user['bmi']}, Category: {user['category']}")


# Formatted Report
print("\n" + "="*50)
print("User Health Report")
print("="*50)

for user in user_data:
    report = (
        f"Name       : {user['name']}\n"
        f"Age        : {user['age']}\n"
        f"BMI        : {user['bmi']}\n"
        f"Category   : {user['category']}\n"
        f"Conditions : {', '.join(user['health_tags'])}\n"
        + "-"*50
    )
    print(report)

#Display unique health conditions
print("\nUnique Health Conditions Across All Users:")
print(", ".join(sorted(all_health_conditions)))
