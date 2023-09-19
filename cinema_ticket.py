day_of_the_week = input()
cinema_ticket = 0

if day_of_the_week == "Monday":
    cinema_ticket = 12
elif day_of_the_week == "Tuesday":
    cinema_ticket = 12
elif day_of_the_week == "Wednesday":
    cinema_ticket = 14
elif day_of_the_week == "Thursday":
    cinema_ticket = 14
elif day_of_the_week == "Friday":
    cinema_ticket = 12
elif day_of_the_week == "Saturday":
    cinema_ticket = 16
elif day_of_the_week == "Sunday":
    cinema_ticket = 16

print(cinema_ticket)