locations = int(input())
total_gold = 0
days = 0

for _ in range(locations):
    expected_average_gold = float(input())
    days = int(input())

    for day in range(days):
        gold = float(input())
        total_gold += gold

    average_gold = total_gold / days

    if average_gold >= expected_average_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        needed_gold = expected_average_gold - average_gold
        print(f"You need {needed_gold:.2f} gold.")

    total_gold = 0
