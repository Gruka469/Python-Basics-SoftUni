chicken = 10.35
fish = 12.40
vegan = 8.15
delivery = 2.50

chicken_amount = int(input())
fish_amount = int(input())
vegan_amount = int(input())

total_without_desert = chicken * chicken_amount + fish * fish_amount + vegan * vegan_amount
desert_price = total_without_desert * 0.20

total = total_without_desert + desert_price

print(total + delivery)