food_quantity = int(input())
total_food_eaten = 0

while True:
    command = input()
    if command == "Adopted":
        break
    food_eaten = int(command)
    total_food_eaten += food_eaten

leftover_food = food_quantity * 1000 - total_food_eaten

if leftover_food >= 0:
    print(f"Food is enough! Leftovers: {leftover_food} grams.")
else:
    needed_food = abs(leftover_food)
    print(f"Food is not enough. You need {needed_food} grams more.")
