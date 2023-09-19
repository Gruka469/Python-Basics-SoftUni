# n = int(input())
# numbers = []


# for _ in range(n):
#     num = int(input())
#     numbers.append(num)

# max_number = max(numbers)
# min_number = min(numbers)

# print(f'Max number: {max_number}')
# print(f'Min number: {min_number}')

import sys 

cound_of_numbers = int(input())

max_number = - sys.maxsize
min_number = sys.maxsize

for number in range(cound_of_numbers):
    numbers = int(input())

if numbers > max_number:
    max_number = numbers

if numbers < min_number:
    min_number = numbers

print(f'Max number {max_number}')
print(f'Min munber {min_number}')