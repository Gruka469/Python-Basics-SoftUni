hour_of_the_day = int(input())
day_of_the_week = input()

if day_of_the_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    if hour_of_the_day >= 10 and hour_of_the_day <= 18:
        print("open")
    else:
        print("closed")

else:
    print("closed")