cat_count = int(input())

group1_count = 0
group2_count = 0
group3_count = 0
total_food_grams = 0

for _ in range(cat_count):
    food_amount = float(input())
    total_food_grams += food_amount

    if 100 <= food_amount < 200:
        group1_count += 1
    elif 200 <= food_amount < 300:
        group2_count += 1
    elif 300 <= food_amount <= 400:
        group3_count += 1

total_food_kg = total_food_grams / 1000
food_price = total_food_kg * 12.45

print(f"Group 1: {group1_count} cats.")
print(f"Group 2: {group2_count} cats.")
print(f"Group 3: {group3_count} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")
