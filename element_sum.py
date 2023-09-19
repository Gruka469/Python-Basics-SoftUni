import sys
max_size = -sys.maxsize
sum_numbers = 0

count_of_numbers = int(input())

for i in range(0, count_of_numbers):
    numbers = int(input())

    if numbers > max_size:
        max_size = numbers

    sum_numbers += numbers

if max_size == sum_numbers - max_size:
    print("Yes")
    print(f'Sum= {sum_numbers}')
else:
    print("No")
    sum_numbers = sum_numbers - max_size
    print(f'Diff= {abs(max_size - sum_numbers)}')
