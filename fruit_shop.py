fruit = input()
day = input()
quantity = float(input())

price = 0

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit.lower() == "banana":
        price = 2.50
    elif fruit.lower() == "apple":
        price = 1.20
    elif fruit.lower() == "orange":
        price = 0.85
    elif fruit.lower() == "grapefruit":
        price = 1.45
    elif fruit.lower() == "kiwi":
        price = 2.70
    elif fruit.lower() == "pineapple":
        price = 5.50
    elif fruit.lower() == "grapes":
        price = 3.85
    else:
        print("error")
        exit()
elif day in ["Saturday", "Sunday"]:
    if fruit.lower() == "banana":
        price = 2.70
    elif fruit.lower() == "apple":
        price = 1.25
    elif fruit.lower() == "orange":
        price = 0.90
    elif fruit.lower() == "grapefruit":
        price = 1.60
    elif fruit.lower() == "kiwi":
        price = 3.00
    elif fruit.lower() == "pineapple":
        price = 5.60
    elif fruit.lower() == "grapes":
        price = 4.20
    else:
        print("error")
        exit()
else:
    print("error")
    exit()

total_price = price * quantity
print(f"{total_price:.2f}")