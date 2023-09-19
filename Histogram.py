def calculate_percentages(numbers):
    n = len(numbers)
    counts = [0, 0, 0, 0, 0]  # Initialize counts for each range

    for num in numbers:
        if num < 200:
            counts[0] += 1
        elif 200 <= num <= 399:
            counts[1] += 1
        elif 400 <= num <= 599:
            counts[2] += 1
        elif 600 <= num <= 799:
            counts[3] += 1
        else:
            counts[4] += 1
    
    percentages = [count / n * 100 for count in counts]
    return percentages

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Calculate percentages
percentages = calculate_percentages(numbers)

# Print the percentages with two decimal places
for p in percentages:
    print(f"{p:.2f}%")
