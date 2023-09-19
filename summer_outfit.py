degrees = int(input())
time_of_the_day = input()
outfit = ""
shoes = ""

if 10 <= degrees <= 18 and time_of_the_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if 10 <= degrees <= 18 and time_of_the_day == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if 10 <= degrees <= 18 and time_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if 18 < degrees <= 24 and time_of_the_day == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if 18 < degrees <= 24 and time_of_the_day == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if 18 < degrees <= 24 and time_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if degrees >= 25 and time_of_the_day == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if degrees >= 25 and time_of_the_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if degrees >= 25 and time_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")