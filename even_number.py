n = int(input())

for i in range(n):
    number = int(input())
    if number % 2 != 0:  # If the number is odd
        print(f'{number} is odd!')
        break

else:
    print("All numbers are even.")
