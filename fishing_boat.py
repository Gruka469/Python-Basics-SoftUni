budget_of_the_group = int(input())
season = input()
fisher_count = int(input())

price_of_boat_rent = 0

if season == "Spring":
    price_of_boat_rent = 3000

if season == "Summer" or season == "Autumn":
    price_of_boat_rent = 4200

if season == "Winter":
    price_of_boat_rent = 2600

if fisher_count <= 6:
    price_of_boat_rent -= price_of_boat_rent * 0.10
elif 7 <= fisher_count <= 11:
    price_of_boat_rent -= price_of_boat_rent * 0.15
elif fisher_count >= 12:
    price_of_boat_rent -= price_of_boat_rent * 0.25

if fisher_count % 2 == 0 and season != "Autumn":
    price_of_boat_rent -= price_of_boat_rent * 0.05

if budget_of_the_group >= price_of_boat_rent:
    left_money = budget_of_the_group - price_of_boat_rent
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = price_of_boat_rent - budget_of_the_group
    print(f"Not enough money! You need {needed_money:.2f} leva.")
