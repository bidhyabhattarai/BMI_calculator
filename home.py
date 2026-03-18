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