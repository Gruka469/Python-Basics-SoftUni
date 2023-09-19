screening_type = input()
rows = int(input())
columns = int(input())
income = 0 
premiere = 12.00
normal = 7.50
discount = 5.00


cinema_capacity = rows * columns

if screening_type == "premiere":
    income = cinema_capacity * 12.00

elif screening_type == "normal":
    income = cinema_capacity * 7.50

elif screening_type == "discount":
    income = cinema_capacity * 5.00

print(f'{income:.2f} leva')


# projection_type = input()
# rows = int(input())
# columns = int(input())

# income = 0

# if projection_type == "Premiere":
#     income = rows * columns * 12.00
# elif projection_type == "Normal":
#     income = rows * columns * 7.50
# elif projection_type == "Discount":
#     income = rows * columns * 5.00

# print(f"{income:.2f} leva")
