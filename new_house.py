flower_type = input()
flower_count = int(input())
budget = int(input())

Roses_price = 5
Dahlias_price = 3.80
Tulips_price = 2.80
Narcissus_price = 3
Gladiolus_price = 2.50

total_price = 0

if flower_type == "Roses":
    total_price = flower_count * Roses_price
    
    if flower_count > 80:
        total_price -= total_price * 0.10

if flower_type == "Dahlias":
    total_price = flower_count * Dahlias_price
    
    if flower_count > 90:
        total_price -= total_price * 0.15

if flower_type == "Tulips":
    total_price = flower_count * Tulips_price
    
    if flower_count > 80:
        total_price -= total_price * 0.15

if flower_type == "Narcissus":
    total_price = flower_count * Narcissus_price
    
    if flower_count < 120:
        total_price += total_price * 0.15

if flower_type == "Gladiolus":
    total_price = flower_count * Gladiolus_price
    
    if flower_count < 80:
        total_price += total_price * 0.20


if budget >= total_price:
    left_money = budget - total_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {left_money:.2f} leva left.")
else:
    needed_money = total_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")