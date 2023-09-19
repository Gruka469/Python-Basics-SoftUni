month = input()
hours = int(input())
people = int(input())
time_of_day = input()

price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price_per_hour = 10.50
    else:
        price_per_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price_per_hour = 12.60
    else:
        price_per_hour = 10.20

total_cost = price_per_hour * hours * people

if people >= 4:
    total_cost -= total_cost * 0.1
if hours >= 5:
    total_cost -= total_cost * 0.5

price_per_person = total_cost / people / hours

print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
